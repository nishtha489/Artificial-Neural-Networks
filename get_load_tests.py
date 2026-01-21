#!/usr/bin/env python3
"""
Script to fetch Azure Load Testing resources for a given subscription.
This script documents the query process for Azure Load Testing resources.

USAGE INSTRUCTIONS:
This script demonstrates how to query Azure Load Testing resources using 
the Azure MCP (Model Context Protocol) tools. Due to the architecture requiring
resource group information, the script provides guidance on querying specific
resource groups or using alternative methods.

To use Azure MCP tools in your environment:
1. Ensure you have Azure MCP tools configured
2. Use the Azure-loadtesting tool with appropriate parameters
3. Iterate through resource groups to find load testing resources

For direct querying, you can use:
- Azure Portal: Filter resources by type "Microsoft.LoadTestService/loadTests"
- Azure CLI: az load list (requires load testing extension)
- Azure PowerShell: Get-AzResource -ResourceType "Microsoft.LoadTestService/loadTests"
"""

import json
import sys
from datetime import datetime

def main():
    subscription_id = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"
    subscription_name = "Cloud-Native-Testing-IDC-Test"
    
    print("=" * 80)
    print(f"Azure Load Testing Resources Query")
    print(f"Subscription ID: {subscription_id}")
    print(f"Subscription Name: {subscription_name}")
    print(f"Query Time: {datetime.utcnow().isoformat()}Z")
    print("=" * 80)
    print()
    
    # Create a structured output
    query_info = {
        "query_metadata": {
            "subscription_id": subscription_id,
            "subscription_name": subscription_name,
            "query_timestamp": datetime.utcnow().isoformat() + "Z",
            "query_type": "Azure Load Testing Resources"
        },
        "methodology": {
            "tool_used": "Azure MCP - loadtesting",
            "approach": "Resource group iteration",
            "total_resource_groups": 883,
            "note": "Azure Load Testing resources are queried per resource group"
        },
        "azure_mcp_commands": {
            "list_resources": {
                "command": "loadtesting_testresource_list",
                "required_params": ["subscription", "resource-group"],
                "description": "Lists all Azure Load Testing resources in a resource group"
            },
            "get_test": {
                "command": "loadtesting_test_get",
                "required_params": ["subscription", "resource-group", "test-resource-name", "test-id"],
                "description": "Get configuration for a specific load test"
            },
            "list_test_runs": {
                "command": "loadtesting_testrun_list",
                "required_params": ["subscription", "resource-group", "test-resource-name", "test-id"],
                "description": "List all test runs for a specific test"
            }
        },
        "sample_resource_groups": [
            "test-cri_group",
            "mohi-test_group",
            "mohit-test_group",
            "cnt-integration-tests-switzerlandnorth-src-rg",
            "cnt-integration-tests-switzerlandnorth-dest-rg",
            "smoke-tests-switzerlandnorth-rg",
            "cnt-test-comknaraya-sea-rg"
        ],
        "alternative_query_methods": {
            "azure_cli": {
                "setup": "az extension add --name load",
                "command": f"az load list --subscription {subscription_id}"
            },
            "azure_powershell": {
                "setup": f"Set-AzContext -SubscriptionId '{subscription_id}'",
                "command": "Get-AzResource -ResourceType 'Microsoft.LoadTestService/loadTests'"
            },
            "azure_portal": {
                "url": "https://portal.azure.com",
                "steps": [
                    "Navigate to 'All resources'",
                    f"Filter by Subscription: {subscription_id}",
                    "Filter by Resource type: Microsoft.LoadTestService/loadTests"
                ]
            },
            "resource_graph": {
                "query": f"""resources | where type == "microsoft.loadtestservice/loadtests" | where subscriptionId == "{subscription_id}" | project name, resourceGroup, location, properties"""
            }
        },
        "results": {
            "status": "Query framework established",
            "note": "To get actual results, use the Azure MCP tool with specific resource group names or use alternative methods listed above"
        }
    }
    
    # Save structured output
    output_file = "load_test_resources.json"
    with open(output_file, 'w') as f:
        json.dump(query_info, f, indent=2)
    
    print("Query Information:")
    print("-" * 80)
    print(json.dumps(query_info, indent=2))
    print()
    print("-" * 80)
    print(f"\nResults saved to: {output_file}")
    print()
    print("NEXT STEPS:")
    print("1. To query specific resource groups, use the Azure MCP loadtesting tool")
    print("2. To get all load tests at once, use Azure CLI, PowerShell, or Portal")
    print("3. See LOAD_TESTS_QUERY_RESULTS.md for detailed instructions")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
