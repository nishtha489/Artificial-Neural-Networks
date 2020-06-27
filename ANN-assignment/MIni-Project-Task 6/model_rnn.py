"""
@author: lilianweng
"""
import numpy as np
import os
import random
import re
import shutil
import time
#import tensorflow as tf
import torch
import matplotlib.pyplot as plt

#from tensorflow.contrib.tensorboard.plugins import projector


import torch
import torch.nn as nn
import torch.autograd as autograd
from torch.autograd import Variable
import numpy as np


class Network(nn.Module):
    def __init__(self, input_size):
        super(Network, self).__init__()
        self.input_size = input_size


        self.LSTM_layer = nn.LSTM(self.input_size, 128, 2)
        self.fc1 = nn.Linear(128, 100)
        self.fc2 = nn.Linear(100, 20)
        self.fc3 = nn.Linear(20, 1)

    def forward(self, x):
        output, hn = self.LSTM_layer(x)
        #print(output.size())
        out = self.fc1(output)
        #print(out.size())
        out = self.fc2(out)
        #print(out.size())
        predict = self.fc3(out)
        return predict

    
