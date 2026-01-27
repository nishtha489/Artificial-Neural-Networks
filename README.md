# Artificial-Neural-Networks

This repository contains educational materials and assignments related to Artificial Neural Networks and Deep Learning.

## Contents

- **ANN-assignment**: Various assignments covering neural network topics
- **Assignment 1 & 2**: Coursework assignments
- **Pytorch_MNIST**: PyTorch implementation for MNIST dataset
- **intro-to-pytorch**: Introduction to PyTorch tutorials

## Documentation

- **[MCP Servers](MCP_SERVERS.md)**: Documentation of available Model Context Protocol servers for development automation
- **[Azure Load Testing](AZURE_LOAD_TESTING.md)**: Integration with Azure Load Testing service

## Azure Load Testing Integration

This repository includes integration with Azure Load Testing service. See [AZURE_LOAD_TESTING.md](AZURE_LOAD_TESTING.md) for details on how to list and manage Azure Load Tests.

### Quick Start

To list Azure Load Tests for a subscription:

```bash
python3 list_load_tests.py --subscription-id 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a
```

Or use the GitHub Actions workflow "List Azure Load Tests" from the Actions tab.

## MCP Servers

This repository development environment has access to several MCP (Model Context Protocol) servers that provide automation capabilities. See [MCP_SERVERS.md](MCP_SERVERS.md) for complete documentation on available servers and their capabilities.