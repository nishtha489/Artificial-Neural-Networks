# Azure Load Testing Integration

This directory contains a script to list Azure Load Tests for a specific subscription.

## Overview

The `list_load_tests.py` script allows you to retrieve all Azure Load Testing resources associated with an Azure subscription ID.

## Prerequisites

1. **Python 3.7 or higher**
2. **Azure Authentication**: You need to be authenticated with Azure. This can be done via:
   - Azure CLI: Run `az login`
   - Service Principal: Set environment variables `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_CLIENT_SECRET`
   - Managed Identity: When running on Azure resources
   - Azure PowerShell: Run `Connect-AzAccount`

## Installation

Install the required dependencies:

```bash
pip install -r requirements-loadtest.txt
```

## Usage

### Using the default subscription ID (7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a):

```bash
python list_load_tests.py
```

### Using a custom subscription ID:

```bash
python list_load_tests.py <your-subscription-id>
```

## Example Output

```
======================================================================
Azure Load Testing - List Load Tests
======================================================================

Fetching load tests for subscription: 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a

Load Test Found:
  Name: my-load-test
  ID: /subscriptions/7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a/resourceGroups/my-rg/providers/Microsoft.LoadTestService/loadtests/my-load-test
  Location: eastus
  Resource Group: my-rg
  Provisioning State: Succeeded

======================================================================
Total load tests found: 1
======================================================================
```

## Authentication

The script uses `DefaultAzureCredential` from the Azure Identity library, which automatically tries multiple authentication methods in the following order:

1. Environment variables
2. Managed Identity
3. Visual Studio Code
4. Azure CLI
5. Azure PowerShell
6. Interactive browser

Make sure you have appropriate permissions to list Load Testing resources in the subscription.

## Permissions Required

The Azure identity you use must have at least **Reader** role on the subscription or resource group containing the Load Testing resources.

## Troubleshooting

- **Authentication Error**: Make sure you're logged in via Azure CLI (`az login`) or have set up service principal credentials
- **Permission Error**: Ensure your account has Reader access to the subscription
- **Subscription Not Found**: Verify the subscription ID is correct and accessible with your credentials
