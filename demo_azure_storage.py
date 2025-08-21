#!/usr/bin/env python3
"""
Demo script showing Azure Storage Account listing functionality

This script demonstrates what the output would look like when the Azure Storage
Account utilities are used with proper authentication.
"""

import json
from azure_storage_utils import AzureStorageManager


def demo_with_mock_data():
    """Demonstrate the functionality with mock data"""
    print("Azure Storage Account Utility - Demo Mode")
    print("=" * 50)
    
    # Create manager instance
    SUBSCRIPTION_ID = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"
    manager = AzureStorageManager(SUBSCRIPTION_ID)
    
    # Mock data that represents typical Azure storage accounts
    mock_storage_accounts = [
        {
            "name": "prodstorageaccount001",
            "resourceGroup": "rg-production",
            "location": "eastus",
            "sku": {"name": "Standard_LRS"},
            "kind": "StorageV2",
            "statusOfPrimary": "available",
            "primaryEndpoints": {
                "blob": "https://prodstorageaccount001.blob.core.windows.net/",
                "file": "https://prodstorageaccount001.file.core.windows.net/",
                "table": "https://prodstorageaccount001.table.core.windows.net/",
                "queue": "https://prodstorageaccount001.queue.core.windows.net/"
            }
        },
        {
            "name": "devstorageaccount002",
            "resourceGroup": "rg-development",
            "location": "westus2",
            "sku": {"name": "Standard_GRS"},
            "kind": "StorageV2",
            "statusOfPrimary": "available",
            "primaryEndpoints": {
                "blob": "https://devstorageaccount002.blob.core.windows.net/",
                "file": "https://devstorageaccount002.file.core.windows.net/",
                "table": "https://devstorageaccount002.table.core.windows.net/",
                "queue": "https://devstorageaccount002.queue.core.windows.net/"
            }
        },
        {
            "name": "datastorageaccount003",
            "resourceGroup": "rg-analytics",
            "location": "centralus",
            "sku": {"name": "Premium_LRS"},
            "kind": "BlockBlobStorage",
            "statusOfPrimary": "available",
            "primaryEndpoints": {
                "blob": "https://datastorageaccount003.blob.core.windows.net/"
            }
        }
    ]
    
    print(f"\nMock Storage Accounts in subscription {SUBSCRIPTION_ID}:")
    print("=" * 80)
    print("(This is demonstration data - actual results require Azure CLI authentication)")
    print()
    
    for i, account in enumerate(mock_storage_accounts, 1):
        print(f"{i}. {account.get('name', 'Unknown')}")
        print(f"   Resource Group: {account.get('resourceGroup', 'Unknown')}")
        print(f"   Location: {account.get('location', 'Unknown')}")
        print(f"   SKU: {account.get('sku', {}).get('name', 'Unknown')}")
        print(f"   Kind: {account.get('kind', 'Unknown')}")
        print(f"   Status: {account.get('statusOfPrimary', 'Unknown')}")
        if account.get('primaryEndpoints'):
            endpoints = account['primaryEndpoints']
            if endpoints.get('blob'):
                print(f"   Blob Endpoint: {endpoints['blob']}")
            if endpoints.get('file'):
                print(f"   File Endpoint: {endpoints['file']}")
            if endpoints.get('table'):
                print(f"   Table Endpoint: {endpoints['table']}")
            if endpoints.get('queue'):
                print(f"   Queue Endpoint: {endpoints['queue']}")
        print()
    
    print(f"Total: {len(mock_storage_accounts)} storage account(s)")
    
    print("\n" + "=" * 80)
    print("To use with real Azure data:")
    print("1. Install Azure CLI: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli")
    print("2. Login to Azure: az login")
    print("3. Run: python3 azure_storage_utils.py")


if __name__ == "__main__":
    demo_with_mock_data()