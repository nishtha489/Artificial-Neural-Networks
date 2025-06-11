#!/usr/bin/env python3
"""
Azure Storage Account Retrieval - Demo

This script demonstrates the expected output format when retrieving storage accounts
for subscription: 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a

This is a demo version that shows sample output format.
"""


def main():
    """Demo function showing expected output format."""
    subscription_id = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"
    
    print(f"Retrieving storage accounts for subscription: {subscription_id}")
    print("-" * 60)
    print("Demo Mode: Showing expected output format")
    print("-" * 60)
    
    # Sample data showing the expected output format
    sample_accounts = [
        {
            'name': 'example-storage-account-1',
            'location': 'East US',
            'resource_group': 'example-rg-1',
            'sku_name': 'Standard_LRS',
            'kind': 'StorageV2',
            'creation_time': '2024-01-15T10:30:00Z',
            'primary_endpoints': {
                'blob': 'https://example-storage-account-1.blob.core.windows.net/',
                'queue': 'https://example-storage-account-1.queue.core.windows.net/',
                'table': 'https://example-storage-account-1.table.core.windows.net/',
                'file': 'https://example-storage-account-1.file.core.windows.net/'
            }
        },
        {
            'name': 'example-storage-account-2',
            'location': 'West US 2',
            'resource_group': 'example-rg-2',
            'sku_name': 'Premium_LRS',
            'kind': 'FileStorage',
            'creation_time': '2024-02-20T14:45:00Z',
            'primary_endpoints': {
                'blob': None,
                'queue': None,
                'table': None,
                'file': 'https://example-storage-account-2.file.core.windows.net/'
            }
        }
    ]
    
    print(f"Found {len(sample_accounts)} storage account(s):")
    print()
    
    for i, account in enumerate(sample_accounts, 1):
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
    
    print("Note: This is demo output. Run 'get_storage_accounts.py' or")
    print("'get_storage_accounts_cli.py' with proper Azure authentication")
    print("to get actual storage account data.")


if __name__ == "__main__":
    main()