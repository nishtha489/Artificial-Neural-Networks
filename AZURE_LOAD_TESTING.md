# Azure Load Testing Integration

This directory contains scripts and workflows for interacting with Azure Load Testing service.

## Overview

The `list_load_tests.py` script allows you to retrieve a list of Azure Load Test resources for a specified subscription ID.

## Prerequisites

- Azure CLI installed and configured
- Appropriate Azure credentials with permissions to access the subscription
- Python 3.6 or higher

## Usage

### Command Line

Run the script directly from the command line:

```bash
# Show version information
python3 list_load_tests.py --version

# List load tests for the default subscription ID (7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a)
python3 list_load_tests.py

# List load tests for a specific subscription ID
python3 list_load_tests.py --subscription-id <your-subscription-id>

# Output results in JSON format
python3 list_load_tests.py --json
```

### GitHub Workflow

You can also trigger the workflow via GitHub Actions:

1. Go to the "Actions" tab in the GitHub repository
2. Select "List Azure Load Tests" workflow
3. Click "Run workflow"
4. (Optional) Enter a custom subscription ID or use the default
5. View the results in the workflow run logs

## Script Details

The `list_load_tests.py` script:

1. Authenticates with Azure (requires Azure CLI to be logged in)
2. Sets the subscription context
3. Queries for all `Microsoft.LoadTestService/loadtests` resources
4. Displays information about each load test including:
   - Name
   - Resource Group
   - Location
   - Resource ID
   - Type

## Example Output

```
Fetching load tests for subscription: 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a
--------------------------------------------------------------------------------
Found 2 load test resource(s):

1. Load Test Resource:
   Name: my-load-test-1
   Resource Group: rg-loadtest
   Location: eastus
   ID: /subscriptions/7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a/resourceGroups/rg-loadtest/providers/Microsoft.LoadTestService/loadtests/my-load-test-1
   Type: Microsoft.LoadTestService/loadtests

2. Load Test Resource:
   Name: my-load-test-2
   Resource Group: rg-loadtest
   Location: westus2
   ID: /subscriptions/7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a/resourceGroups/rg-loadtest/providers/Microsoft.LoadTestService/loadtests/my-load-test-2
   Type: Microsoft.LoadTestService/loadtests
```

## Authentication

When running locally, ensure you're logged in to Azure CLI:

```bash
az login
```

When running in GitHub Actions, the workflow uses federated credentials configured through the repository secrets:
- `AZURE_CLIENT_ID`
- `AZURE_TENANT_ID`

## Troubleshooting

- **Authentication Error**: Make sure you're logged in to Azure CLI with `az login`
- **Permission Error**: Ensure your Azure account has read permissions on the subscription
- **No Load Tests Found**: The subscription may not have any Azure Load Testing resources deployed
