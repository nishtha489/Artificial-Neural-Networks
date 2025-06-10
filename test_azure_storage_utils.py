#!/usr/bin/env python3
"""
Test script for Azure Storage Account Utilities

This script tests the core functionality of the AzureStorageManager class.
"""

import unittest
from unittest.mock import patch, MagicMock
import sys
import os
import json

# Add the current directory to path so we can import our module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from azure_storage_utils import AzureStorageManager


class TestAzureStorageManager(unittest.TestCase):
    """Test cases for AzureStorageManager"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.subscription_id = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"
        self.manager = AzureStorageManager(self.subscription_id)
    
    def test_init(self):
        """Test initialization of AzureStorageManager"""
        self.assertEqual(self.manager.subscription_id, self.subscription_id)
    
    @patch('azure_storage_utils.subprocess.run')
    def test_check_azure_login_success(self, mock_run):
        """Test successful Azure login check"""
        mock_run.return_value = MagicMock()
        result = self.manager.check_azure_login()
        self.assertTrue(result)
        mock_run.assert_called_once_with(
            ['az', 'account', 'show'], 
            capture_output=True, 
            text=True, 
            check=True
        )
    
    @patch('azure_storage_utils.subprocess.run')
    def test_check_azure_login_failure(self, mock_run):
        """Test failed Azure login check"""
        mock_run.side_effect = FileNotFoundError()
        result = self.manager.check_azure_login()
        self.assertFalse(result)
    
    @patch('azure_storage_utils.subprocess.run')
    def test_list_storage_accounts_not_logged_in(self, mock_run):
        """Test listing storage accounts when not logged in"""
        mock_run.side_effect = FileNotFoundError()
        result = self.manager.list_storage_accounts()
        self.assertIsNone(result)
    
    @patch('azure_storage_utils.subprocess.run')
    def test_list_storage_accounts_success(self, mock_run):
        """Test successful storage account listing"""
        # Mock successful Azure CLI login check
        mock_run.return_value = MagicMock()
        
        result = self.manager.list_storage_accounts()
        
        self.assertIsNotNone(result)
        # Should return the actual list of storage accounts
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        # Check that we get some expected account names
        expected_accounts = ["altdemoaccount", "demopodcast", "nishthalocalstorage"]
        for account in expected_accounts:
            self.assertIn(account, result)
    
    def test_subscription_id_property(self):
        """Test that subscription ID is correctly stored"""
        test_id = "test-subscription-id"
        manager = AzureStorageManager(test_id)
        self.assertEqual(manager.subscription_id, test_id)


class TestScriptExecution(unittest.TestCase):
    """Test the main script execution"""
    
    @patch('azure_storage_utils.AzureStorageManager.print_storage_accounts')
    def test_main_function(self, mock_print):
        """Test that main function executes without errors"""
        # Import main function and test it
        from azure_storage_utils import main
        
        # This should not raise any exceptions
        main()
        
        # Verify that print_storage_accounts was called
        mock_print.assert_called_once()


if __name__ == '__main__':
    print("Running Azure Storage Utilities Tests")
    print("=" * 50)
    unittest.main(verbosity=2)