#!/usr/bin/env python3
"""
Script to list Azure Load Tests for a specific subscription ID.

This script authenticates with Azure using DefaultAzureCredential and 
lists all load tests associated with the provided subscription ID.
"""

import sys
from azure.identity import DefaultAzureCredential
from azure.mgmt.loadtesting import LoadTestMgmtClient

def list_load_tests(subscription_id):
    """
    List all Azure Load Tests for the given subscription ID.
    
    Args:
        subscription_id (str): Azure subscription ID
        
    Returns:
        list: List of load test resources
    """
    # Authenticate using DefaultAzureCredential
    # This supports various authentication methods including:
    # - Environment variables
    # - Managed identity
    # - Azure CLI
    # - Azure PowerShell
    credential = DefaultAzureCredential()
    
    # Create the Load Testing management client
    client = LoadTestMgmtClient(credential, subscription_id)
    
    # List all load test resources in the subscription
    load_tests = []
    print(f"Fetching load tests for subscription: {subscription_id}\n")
    
    try:
        # List all load testing resources across all resource groups
        for load_test in client.load_tests.list_by_subscription():
            load_tests.append(load_test)
            print(f"Load Test Found:")
            print(f"  Name: {load_test.name}")
            print(f"  ID: {load_test.id}")
            print(f"  Location: {load_test.location}")
            print(f"  Resource Group: {load_test.id.split('/')[4]}")
            if hasattr(load_test, 'provisioning_state'):
                print(f"  Provisioning State: {load_test.provisioning_state}")
            print()
            
    except Exception as e:
        print(f"Error listing load tests: {e}", file=sys.stderr)
        raise
    
    return load_tests

def main():
    """Main function to run the script."""
    # Default subscription ID from the issue
    subscription_id = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"
    
    # Allow override via command line argument
    if len(sys.argv) > 1:
        subscription_id = sys.argv[1]
    
    print("=" * 70)
    print("Azure Load Testing - List Load Tests")
    print("=" * 70)
    print()
    
    load_tests = list_load_tests(subscription_id)
    
    print("=" * 70)
    print(f"Total load tests found: {len(load_tests)}")
    print("=" * 70)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
