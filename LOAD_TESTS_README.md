# Load Test Management System

This module provides functionality to manage and organize load tests for neural network models, organized by subscription IDs.

## Overview

The Load Test Management System allows you to:
- Organize performance and load tests by subscription ID
- Retrieve lists of tests for specific subscriptions
- Add new load tests to subscriptions
- Support for various neural network model types (CNN, RNN, Autoencoder, Seq2Seq, MLP, etc.)

## Usage

### Command Line Interface

Get load tests for the default subscription ID:
```bash
python get_load_tests.py
```

Get load tests for a specific subscription ID:
```bash
python get_load_tests.py <subscription_id>
```

Get output in JSON format:
```bash
python get_load_tests.py <subscription_id> --json
```

### Python API

```python
from load_test_manager import get_load_tests_for_subscription, LoadTestManager, LoadTest

# Get tests for a subscription
subscription_id = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"
tests = get_load_tests_for_subscription(subscription_id)

# Create a new load test
new_test = LoadTest(
    test_id="lt_custom",
    name="Custom Performance Test",
    model_type="CNN",
    test_type="performance"
)

# Add to subscription
manager = LoadTestManager()
manager.add_load_test(subscription_id, new_test)
```

## Default Test Data

The system comes pre-configured with sample load tests for subscription ID `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`:

1. **PyTorch CNN Performance Test** - CNN performance testing
2. **RNN Sentiment Analysis Load Test** - RNN load testing  
3. **Autoencoder Compression Benchmark** - Autoencoder benchmarking
4. **Seq2Seq Translation Performance** - Seq2Seq performance testing
5. **MNIST Classification Stress Test** - MLP stress testing

## Test Types

Supported test types include:
- `performance` - Performance evaluation tests
- `load` - Load testing for high-volume scenarios
- `benchmark` - Benchmarking against standards
- `stress` - Stress testing under extreme conditions
- `unit_test` - Unit testing for specific components

## Model Types

Supported neural network model types:
- `CNN` - Convolutional Neural Networks
- `RNN` - Recurrent Neural Networks  
- `MLP` - Multi-Layer Perceptrons
- `Autoencoder` - Autoencoder networks
- `Seq2Seq` - Sequence-to-Sequence models
- Custom model types as needed

## Files

- `load_test_manager.py` - Core load test management functionality
- `get_load_tests.py` - Command-line interface
- `test_load_manager.py` - Test suite for validation
- `LOAD_TESTS_README.md` - This documentation

## Testing

Run the test suite to validate functionality:
```bash
python test_load_manager.py
```

This will test all core functionality including:
- Retrieving tests for subscriptions
- Adding new tests
- Data structure validation
- Edge case handling