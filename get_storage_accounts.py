#!/usr/bin/env python3
"""
Azure Storage Account Retrieval Script

This script retrieves the list of storage accounts for a specific Azure subscription.
It demonstrates how to use Azure SDK to connect to Azure and list storage accounts.

Required: Azure CLI authentication (run 'az login' first)
Subscription ID: 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a
"""

import sys
from typing import List, Dict, Any

try:
    from azure.identity import DefaultAzureCredential
    from azure.mgmt.storage import StorageManagementClient
    from azure.core.exceptions import ClientAuthenticationError
except ImportError:
    print("Azure SDK libraries not installed. Install with:")
    print("pip install azure-identity azure-mgmt-storage")
    sys.exit(1)


def get_storage_accounts(subscription_id: str) -> List[Dict[str, Any]]:
    """
    Retrieve storage accounts for the specified Azure subscription.
    
    Args:
        subscription_id (str): Azure subscription ID
        
    Returns:
        List[Dict[str, Any]]: List of storage account information
    """
    try:
        # Create credential and storage client
        credential = DefaultAzureCredential()
        storage_client = StorageManagementClient(credential, subscription_id)
        
        # Get list of storage accounts
        storage_accounts = []
        for account in storage_client.storage_accounts.list():
            account_info = {
                'name': account.name,
                'location': account.location,
                'resource_group': account.id.split('/')[4],  # Extract resource group from resource ID
                'sku_name': account.sku.name,
                'kind': account.kind,
                'creation_time': account.creation_time.isoformat() if account.creation_time else None,
                'primary_endpoints': {
                    'blob': account.primary_endpoints.blob if account.primary_endpoints else None,
                    'queue': account.primary_endpoints.queue if account.primary_endpoints else None,
                    'table': account.primary_endpoints.table if account.primary_endpoints else None,
                    'file': account.primary_endpoints.file if account.primary_endpoints else None,
                } if account.primary_endpoints else None
            }
            storage_accounts.append(account_info)
            
        return storage_accounts
        
    except ClientAuthenticationError:
        print("Authentication failed. Please run 'az login' to authenticate with Azure.")
        sys.exit(1)
    except Exception as e:
        print(f"Error retrieving storage accounts: {str(e)}")
        sys.exit(1)


def main():
    """Main function to retrieve and display storage accounts."""
    subscription_id = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"
    
    print(f"Retrieving storage accounts for subscription: {subscription_id}")
    print("-" * 60)
    
    storage_accounts = get_storage_accounts(subscription_id)
    
    if not storage_accounts:
        print("No storage accounts found in this subscription.")
        return
    
    print(f"Found {len(storage_accounts)} storage account(s):")
    print()
    
    for i, account in enumerate(storage_accounts, 1):
        print(f"{i}. Storage Account: {account['name']}")
        print(f"   Location: {account['location']}")
        print(f"   Resource Group: {account['resource_group']}")
        print(f"   SKU: {account['sku_name']}")
        print(f"   Kind: {account['kind']}")
        if account['creation_time']:
            print(f"   Created: {account['creation_time']}")
        if account['primary_endpoints'] and account['primary_endpoints']['blob']:
            print(f"   Blob Endpoint: {account['primary_endpoints']['blob']}")
        print()


if __name__ == "__main__":
    main()