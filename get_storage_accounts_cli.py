#!/usr/bin/env python3
"""
Azure Storage Account Retrieval - CLI Alternative

This script uses Azure CLI commands to retrieve storage accounts.
Alternative approach when Azure SDK Python libraries are not available.

Required: Azure CLI installed and authenticated (run 'az login' first)
Subscription ID: 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a
"""

import subprocess
import json
import sys


def run_az_command(command: list) -> dict:
    """
    Run Azure CLI command and return parsed JSON output.
    
    Args:
        command (list): Azure CLI command as list of strings
        
    Returns:
        dict: Parsed JSON response
    """
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Azure CLI command failed: {e}")
        print(f"Command: {' '.join(command)}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON output: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("Azure CLI not found. Please install Azure CLI:")
        print("https://docs.microsoft.com/en-us/cli/azure/install-azure-cli")
        sys.exit(1)


def get_storage_accounts_cli(subscription_id: str) -> list:
    """
    Get storage accounts using Azure CLI.
    
    Args:
        subscription_id (str): Azure subscription ID
        
    Returns:
        list: List of storage accounts
    """
    command = [
        'az', 'storage', 'account', 'list',
        '--subscription', subscription_id,
        '--output', 'json'
    ]
    
    return run_az_command(command)


def main():
    """Main function to retrieve and display storage accounts using Azure CLI."""
    subscription_id = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"
    
    print(f"Retrieving storage accounts for subscription: {subscription_id}")
    print("Using Azure CLI...")
    print("-" * 60)
    
    storage_accounts = get_storage_accounts_cli(subscription_id)
    
    if not storage_accounts:
        print("No storage accounts found in this subscription.")
        return
    
    print(f"Found {len(storage_accounts)} storage account(s):")
    print()
    
    for i, account in enumerate(storage_accounts, 1):
        print(f"{i}. Storage Account: {account.get('name', 'N/A')}")
        print(f"   Location: {account.get('location', 'N/A')}")
        print(f"   Resource Group: {account.get('resourceGroup', 'N/A')}")
        
        sku = account.get('sku', {})
        print(f"   SKU: {sku.get('name', 'N/A')}")
        
        print(f"   Kind: {account.get('kind', 'N/A')}")
        
        if 'creationTime' in account:
            print(f"   Created: {account['creationTime']}")
            
        primary_endpoints = account.get('primaryEndpoints', {})
        if primary_endpoints.get('blob'):
            print(f"   Blob Endpoint: {primary_endpoints['blob']}")
            
        print()


if __name__ == "__main__":
    main()