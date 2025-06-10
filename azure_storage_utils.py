#!/usr/bin/env python3
"""
Azure Storage Account Utilities

This script provides functionality to list Azure storage accounts for a given subscription.
Requires Azure CLI to be installed and authenticated.
"""

import subprocess
import json
import sys
from typing import List, Dict, Optional


class AzureStorageManager:
    """Manager class for Azure Storage operations"""
    
    def __init__(self, subscription_id: str):
        """
        Initialize the Azure Storage Manager
        
        Args:
            subscription_id (str): Azure subscription ID
        """
        self.subscription_id = subscription_id
    
    def check_azure_login(self) -> bool:
        """
        Check if user is logged into Azure CLI
        
        Returns:
            bool: True if logged in, False otherwise
        """
        try:
            result = subprocess.run(
                ['az', 'account', 'show'], 
                capture_output=True, 
                text=True, 
                check=True
            )
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def list_storage_accounts(self) -> Optional[List[Dict]]:
        """
        List all storage accounts in the subscription
        
        Returns:
            List[Dict]: List of storage account details or None if error
        """
        if not self.check_azure_login():
            print("Error: Not logged into Azure CLI. Please run 'az login' first.")
            return None
        
        try:
            # Set the subscription
            subprocess.run(
                ['az', 'account', 'set', '--subscription', self.subscription_id],
                capture_output=True,
                text=True,
                check=True
            )
            
            # List storage accounts
            result = subprocess.run(
                ['az', 'storage', 'account', 'list', '--output', 'json'],
                capture_output=True,
                text=True,
                check=True
            )
            
            storage_accounts = json.loads(result.stdout)
            return storage_accounts
            
        except subprocess.CalledProcessError as e:
            print(f"Error listing storage accounts: {e}")
            print(f"Error output: {e.stderr}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON response: {e}")
            return None
    
    def print_storage_accounts(self) -> None:
        """Print storage accounts in a readable format"""
        storage_accounts = self.list_storage_accounts()
        
        if storage_accounts is None:
            return
        
        if not storage_accounts:
            print(f"No storage accounts found in subscription {self.subscription_id}")
            return
        
        print(f"\nStorage Accounts in subscription {self.subscription_id}:")
        print("=" * 80)
        
        for i, account in enumerate(storage_accounts, 1):
            print(f"\n{i}. {account.get('name', 'Unknown')}")
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
        
        print(f"\nTotal: {len(storage_accounts)} storage account(s)")


def main():
    """Main function to demonstrate usage"""
    # The subscription ID from the issue
    SUBSCRIPTION_ID = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"
    
    print("Azure Storage Account Utility")
    print("=" * 40)
    
    # Create manager instance
    manager = AzureStorageManager(SUBSCRIPTION_ID)
    
    # List and display storage accounts
    manager.print_storage_accounts()


if __name__ == "__main__":
    main()