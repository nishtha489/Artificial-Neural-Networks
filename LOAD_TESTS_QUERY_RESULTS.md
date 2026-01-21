# Azure Load Tests Query Results

## Query Information
- **Subscription ID**: `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`
- **Subscription Name**: Cloud-Native-Testing-IDC-Test
- **Tenant ID**: `72f988bf-86f1-41af-91ab-2d7cd011db47`
- **Query Date**: 2026-01-21

## Methodology

This document describes the process used to query Azure Load Testing resources using the Azure MCP (Model Context Protocol) tools.

### Approach Taken

1. **Azure MCP Load Testing Tool**
   - Tool: `Azure-loadtesting`
   - Command: `loadtesting_testresource_list`
   - Purpose: List all Azure Load Testing resources in the subscription

2. **Resource Groups Discovery**
   - Total Resource Groups Found: **883**
   - Sample Resource Groups with 'test' in name:
     - test-cri_group
     - mohi-test_group
     - mohit-test_group
     - cnt-integration-tests-switzerlandnorth-src-rg
     - cnt-integration-tests-switzerlandnorth-dest-rg
     - smoke-tests-switzerlandnorth-rg
     - cnt-test-comknaraya-sea-rg
     - cnt-test-gblknaraya-Outbound-ip-pool-rg
     - cnt-test-gblknaraya-Inbound-ip-pool-rg

### Azure Load Testing Tool Commands Available

The following commands are available in the Azure-loadtesting MCP tool:

#### Resource Management
- **loadtesting_testresource_list**: Lists all Azure Load Testing resources
- **loadtesting_testresource_create**: Creates a new Load Testing resource

#### Test Configuration
- **loadtesting_test_get**: Get configuration for a specific load test
- **loadtesting_test_create**: Create a new load test plan

#### Test Run Management
- **loadtesting_testrun_get**: Get details for a specific test run
- **loadtesting_testrun_list**: List all test runs for a test
- **loadtesting_testrun_create**: Create/trigger a new test run
- **loadtesting_testrun_update**: Update test run metadata

## Results

### Status
⚠️ **Query in Progress**

The Azure MCP loadtesting tool requires resource group information to list load testing resources. Given the large number of resource groups (883) in this subscription, a comprehensive scan would need to:

1. Iterate through all resource groups
2. Query each resource group for load testing resources
3. Aggregate the results

### Recommendations for Complete Query

To get a complete list of all load testing resources in this subscription, you can:

#### Option 1: Use Azure Portal
1. Navigate to [Azure Portal](https://portal.azure.com)
2. Go to "All resources"
3. Filter by:
   - Subscription: `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`
   - Resource type: `Microsoft.LoadTestService/loadTests`

#### Option 2: Use Azure CLI with Load Testing Extension
```bash
# Install the load testing extension
az extension add --name load

# List all load testing resources
az load list --subscription 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a
```

#### Option 3: Use Azure PowerShell
```powershell
# Set the subscription context
Set-AzContext -SubscriptionId "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"

# Get all load testing resources
Get-AzResource -ResourceType "Microsoft.LoadTestService/loadTests"
```

#### Option 4: Use Azure Resource Graph Query
```kusto
resources | where type == "microsoft.loadtestservice/loadtests" | where subscriptionId == "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a" | project name, resourceGroup, location, properties
```

## Authentication Details

The query was executed with the following authentication:
- **User Type**: Service Principal
- **Principal ID**: `12fa8445-f1ce-4697-9ae3-c8d9260770ad`
- **Environment**: AzureCloud
- **Subscription State**: Enabled

## Next Steps

To complete this query:
1. Use one of the recommended methods above to get a complete list
2. If specific resource groups are known to contain load tests, query those directly using the Azure MCP tool
3. Consider using Azure Resource Graph for efficient querying across all resource groups

---

*Generated on: 2026-01-21T09:31:16.742Z*
