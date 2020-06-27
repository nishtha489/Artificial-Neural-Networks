import os
import pandas as pd
import pprint
import matplotlib.pyplot as plt
import numpy as np
import torch
import random
#import tensorflow as tf
#import tensorflow.contrib.slim as slim
#import absl as flags
import torch.autograd as autograd
import torch.nn as nn
import torch.optim as optim
#import torch.autograd as Variable
from model_rnn import Network
from data_model import StockDataSet
from model_rnn import Network

class RNNConfig():
    input_size = 1
    num_steps = 30
    lstm_size = 128
    num_layers = 1
    keep_prob = 0.8

    batch_size = 64
    init_learning_rate = 0.001
    learning_rate_decay = 0.99
    init_epoch = 5
    max_epoch = 50

    def to_dict(self):
        dct = self.__class__.__dict__
        return {k: v for k, v in dct.items() if not k.startswith('__') and not callable(v)}

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return str(self.to_dict())


DEFAULT_CONFIG = RNNConfig()
print( "Default configuration:", DEFAULT_CONFIG.to_dict())

DATA_DIR = "data"
LOG_DIR = "logs"
MODEL_DIR = "models"
stock_symbol = ""
stock_count = 100
input_size = 1
num_steps = 30
lstm_size = 128
num_layers = 1
keep_prob = 0.8

batch_size = 64
init_learning_rate = 0.001
learning_rate_decay = 0.99
init_epoch = 5
max_epoch = 50
pp = pprint.PrettyPrinter()

if not os.path.exists("logs"):
    os.mkdir("logs")


def load_sp500(input_size, num_steps, k=None, target_symbol=None, test_ratio=0.05):
    if target_symbol is not None:
        return [
            StockDataSet(
                target_symbol,
                input_size=input_size,
                num_steps=num_steps,
                test_ratio=test_ratio)
        ]

    # Load metadata of s & p 500 stocks
    info = pd.read_csv("data/constituents-financials.csv")
    info = info.rename(columns={col: col.lower().replace(' ', '_') for col in info.columns})
    info['file_exists'] = info['symbol'].map(lambda x: os.path.exists("data/{}.csv".format(x)))
    print (info['file_exists'].value_counts().to_dict())

    info = info[info['file_exists'] == True].reset_index(drop=True)
    info = info.sort('market_cap', ascending=False).reset_index(drop=True)

    if k is not None:
        info = info.head(k)

    print ("Head of S&P 500 info:\n", info.head())

    # Generate embedding meta file
    info[['symbol', 'sector']].to_csv(os.path.join("logs/metadata.tsv"), sep='\t', index=False)

    return [
        StockDataSet(row['symbol'],
                     input_size=input_size,
                     num_steps=num_steps,
                     test_ratio=0.05)
        for _, row in info.iterrows()]

def train(dataset_list, config):

    merged_test_X = []
    merged_test_y = []
    merged_test_labels = []

    for label_, d_ in enumerate(dataset_list):
        merged_test_X += list(d_.test_X)
        merged_test_y += list(d_.test_y)
        merged_test_labels += [[label_]] * len(d_.test_X)

    merged_test_X = np.array(merged_test_X)
    merged_test_y = np.array(merged_test_y)
    merged_test_labels = np.array(merged_test_labels)

    print ("len(merged_test_X) =", len(merged_test_X))
    print ("len(merged_test_y) =", len(merged_test_y))
    print ("len(merged_test_labels) =", len(merged_test_labels))

    global_step = 0

    num_batches = sum(len(d_.train_X) for d_ in dataset_list) // config.batch_size
   # random.seed(time.time())

    # Select samples for plotting.
    sample_labels = range(min(config.sample_size, len(dataset_list)))
    sample_indices = {}
    for l in sample_labels:
        sym = dataset_list[l].stock_sym
        target_indices = np.array([
            i for i, sym_label in enumerate(merged_test_labels)
            if sym_label[0] == l])
        sample_indices[sym] = target_indices
    print (sample_indices)

    print ("Start training for stocks:", [d.stock_sym for d in dataset_list])
    for epoch in range(config.max_epoch):
        epoch_step = 0
        learning_rate = config.init_learning_rate * (
            config.learning_rate_decay ** max(float(epoch + 1 - config.init_epoch), 0.0)
        )

        for label_, d_ in enumerate(dataset_list):
            running_loss = 0
            for batch_X, batch_y in d_.generate_one_epoch(config.batch_size):
                global_step += 1
                loss = 0
                epoch_step += 1
                batch_labels = np.array([[label_]] * len(batch_X))
                optimizer.zero_grad()
                logits = model(input_size, num_layers, lstm_size, keep_prob)
                loss = loss(logits, label_)
                loss.backward()
                optimizer.step()
                running_loss += loss.item()
                if np.mod(global_step, len(dataset_list) * 200 / config.input_size) == 1:
                    print ("Step:%d [Epoch:%d] [Learning rate: %.6f] train_loss:%.6f test_loss:%.6f" % (
                        global_step, epoch, learning_rate, running_loss, loss))

    return


@property
def model_name(self):
    name = "stock_rnn_lstm%d_step%d_input%d" % (
        self.lstm_size, self.num_steps, self.input_size)

    if self.embed_size > 0:
        name += "_embed%d" % self.embed_size

    return name

@property
def model_logs_dir(self):
    model_logs_dir = os.path.join(self.logs_dir, self.model_name)
    if not os.path.exists(model_logs_dir):
        os.makedirs(model_logs_dir)
    return model_logs_dir

@property
def model_plots_dir(self):
    model_plots_dir = os.path.join(self.plots_dir, self.model_name)
    if not os.path.exists(model_plots_dir):
        os.makedirs(model_plots_dir)
    return model_plots_dir


def plot_samples(self, preds, targets, figname, stock_sym=None, multiplier=5):
    def _flatten(seq):
        return np.array([x for y in seq for x in y])

    truths = _flatten(targets)[-200:]
    preds = (_flatten(preds) * multiplier)[-200:]
    days = range(len(truths))[-200:]

    plt.figure(figsize=(12, 6))
    plt.plot(days, truths, label='truth')
    plt.plot(days, preds, label='pred')
    plt.legend(loc='upper left', frameon=False)
    plt.xlabel("day")
    plt.ylabel("normalized price")
    plt.ylim((min(truths), max(truths)))
    plt.grid(ls='--')

    if stock_sym:
        plt.title(stock_sym + " | Last %d days in test" % len(truths))

    plt.savefig(figname, format='png', bbox_inches='tight', transparent=True)
    plt.close()


if __name__ == '__main__':
        from torch import nn
        model = Network(input_size)
        stock_data_list = load_sp500(
            input_size,
            num_steps,
            k=stock_count,
            target_symbol=stock_symbol,
        )
        loss_function = nn.MSELoss()
        config = RNNConfig()
        optimizer = optim.Adam(model.parameters(), lr=0.1)


        global_step = 0
        epoch_step = 0

        for epoch in range(5):
            running_loss = 0
            for label_, d_ in enumerate(stock_data_list):
                for batch_X, batch_y in d_.generate_one_epoch(config.batch_size):
                    global_step += 1
                    epoch_step += 1
                    x = torch.Tensor(batch_X)
                    batch_labels = torch.Tensor(batch_y)
                    batch_labels = batch_labels.view((batch_labels.shape[1], -1))
                    #print(x.size(), batch_labels.size())
                    optimizer.zero_grad()
                    logits = model(x)
                    #print(logits.view(64,1).size())
                    loss = loss_function(logits, batch_labels)
                    loss.backward()
                    optimizer.step()
                    running_loss += loss.item()
                    if np.mod(global_step, len(stock_data_list) * 200 / config.input_size) == 1:
                        print ("Step:%d [Epoch:%d] loss:%.6f" % (
                            global_step, epoch, loss))
