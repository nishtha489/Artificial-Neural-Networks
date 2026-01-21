# Azure Load Testing Resources Query

## Overview
This repository contains scripts and documentation for querying Azure Load Testing resources using the Azure MCP (Model Context Protocol) tools.

## Query Details
- **Subscription ID**: `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`
- **Subscription Name**: Cloud-Native-Testing-IDC-Test
- **Total Resource Groups**: 883
- **Query Date**: 2026-01-21

## Files in This Repository

### 1. LOAD_TESTS_QUERY_RESULTS.md
Comprehensive documentation explaining:
- Query methodology
- Available Azure MCP loadtesting commands
- Alternative querying methods (Azure CLI, PowerShell, Portal, Resource Graph)
- Step-by-step instructions for different approaches

### 2. get_load_tests.py
Python script that:
- Documents the query process for Azure Load Testing resources
- Generates structured JSON output with query metadata
- Provides usage instructions and examples
- Lists alternative query methods

**Usage:**
```bash
python3 get_load_tests.py
```

**Output:** `load_test_resources.json`

### 3. query_load_tests.sh
Shell script that:
- Demonstrates systematic querying across resource groups
- Documents the process for checking load testing resources
- Provides example Azure MCP command usage

**Usage:**
```bash
chmod +x query_load_tests.sh
./query_load_tests.sh
```

**Output:** `load_testing_resources_found.txt`

### 4. load_test_resources.json
Structured JSON output containing:
- Query metadata (subscription, timestamp, etc.)
- Methodology documentation
- Azure MCP command reference
- Sample resource groups
- Alternative query methods
- Resource Graph query examples

## How to Query Load Testing Resources

### Method 1: Using Azure MCP Tools (Recommended for this environment)

The Azure MCP loadtesting tool provides commands to query load testing resources:

```python
# List all load testing resources in a resource group
Azure-loadtesting command: loadtesting_testresource_list
Parameters: {
  "subscription": "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a",
  "resource-group": "<resource-group-name>"
}
```

**Note**: The loadtesting tool requires a resource group parameter, so you need to iterate through resource groups to find all load testing resources.

### Method 2: Using Azure CLI

```bash
# Install the load testing extension
az extension add --name load

# List all load testing resources
az load list --subscription 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a
```

### Method 3: Using Azure PowerShell

```powershell
# Set the subscription context
Set-AzContext -SubscriptionId "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"

# Get all load testing resources
Get-AzResource -ResourceType "Microsoft.LoadTestService/loadTests"
```

### Method 4: Using Azure Portal

1. Navigate to https://portal.azure.com
2. Go to "All resources"
3. Filter by:
   - Subscription: `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`
   - Resource type: `Microsoft.LoadTestService/loadTests`

### Method 5: Using Azure Resource Graph

```kusto
resources
| where type == "microsoft.loadtestservice/loadtests"
| where subscriptionId == "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"
| project name, resourceGroup, location, properties
```

## Azure MCP Loadtesting Commands Reference

### Resource Management
- `loadtesting_testresource_list` - Lists all Azure Load Testing resources in a resource group
- `loadtesting_testresource_create` - Creates a new Load Testing resource

### Test Configuration
- `loadtesting_test_get` - Get configuration for a specific load test
- `loadtesting_test_create` - Create a new load test plan

### Test Run Management
- `loadtesting_testrun_get` - Get details for a specific test run
- `loadtesting_testrun_list` - List all test runs for a test
- `loadtesting_testrun_create` - Create/trigger a new test run
- `loadtesting_testrun_update` - Update test run metadata

## Sample Resource Groups

The following resource groups contain "test" in their names and may contain load testing resources:
- test-cri_group
- mohi-test_group
- mohit-test_group
- cnt-integration-tests-switzerlandnorth-src-rg
- cnt-integration-tests-switzerlandnorth-dest-rg
- smoke-tests-switzerlandnorth-rg
- cnt-test-comknaraya-sea-rg

## Authentication

The query was executed with:
- **User Type**: Service Principal
- **Principal ID**: `12fa8445-f1ce-4697-9ae3-c8d9260770ad`
- **Tenant ID**: `72f988bf-86f1-41af-91ab-2d7cd011db47`
- **Environment**: AzureCloud
- **Subscription State**: Enabled

## Next Steps

To get actual load testing resource details:

1. **For specific resource groups**: Use the Azure MCP loadtesting tool with the `loadtesting_testresource_list` command and specify the resource group name.

2. **For all resources at once**: Use Azure CLI with the load testing extension, Azure PowerShell, or Azure Portal as documented above.

3. **For automated queries**: Use the Azure Resource Graph query to get all load testing resources in a single query.

## Troubleshooting

If you encounter issues:
- Ensure proper Azure authentication is configured
- Verify you have the necessary permissions to list resources in the subscription
- Check that resource group names are correct (they are case-sensitive)
- For Azure MCP tool issues, refer to: https://aka.ms/azmcp/troubleshooting

## Summary

This repository provides a comprehensive framework for querying Azure Load Testing resources using multiple methods. The scripts demonstrate the query process and provide structured output that can be used for further analysis or automation.

For the subscription `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`, you can use any of the documented methods to retrieve the complete list of load testing resources.

---

*Last Updated: 2026-01-21*
