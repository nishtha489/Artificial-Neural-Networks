# Azure Storage Account Utilities

This utility script provides functionality to list Azure storage accounts for a specific subscription.

## Prerequisites

1. **Azure CLI**: Install the Azure CLI on your system
   - Windows: Download from [Azure CLI installer](https://aka.ms/installazurecliwindows)
   - macOS: `brew install azure-cli`
   - Linux: Follow instructions at [Install Azure CLI on Linux](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-linux)

2. **Authentication**: Login to Azure CLI
   ```bash
   az login
   ```

3. **Python 3.x**: Ensure Python 3.x is installed

## Usage

### Command Line
Run the script directly to list storage accounts for the pre-configured subscription:

```bash
python3 azure_storage_utils.py
```

### As a Module
You can also import and use the `AzureStorageManager` class in your own scripts:

```python
from azure_storage_utils import AzureStorageManager

# Initialize with your subscription ID
manager = AzureStorageManager("your-subscription-id")

# List storage accounts
accounts = manager.list_storage_accounts()

# Print formatted output
manager.print_storage_accounts()
```

## Subscription Information

This script is configured to work with subscription ID: `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`

## Output Format

The script displays the following information for each storage account:
- Account Name
- Resource Group
- Location
- SKU (pricing tier)
- Kind (storage account type)
- Status
- Primary Endpoints (Blob, File, Table, Queue)

## Error Handling

The script includes comprehensive error handling for:
- Azure CLI authentication issues
- Network connectivity problems
- JSON parsing errors
- Subscription access permissions

## Troubleshooting

1. **Authentication Errors**: Ensure you're logged in with `az login`
2. **Permission Errors**: Verify you have appropriate permissions for the subscription
3. **Subscription Not Found**: Check that the subscription ID is correct and accessible
4. **Azure CLI Not Found**: Install Azure CLI following the prerequisites above

## Example Output

```
Azure Storage Account Utility
========================================

Storage Accounts in subscription 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a:
================================================================================

1. mystorageaccount001
   Resource Group: rg-production
   Location: East US
   SKU: Standard_LRS
   Kind: StorageV2
   Status: available
   Blob Endpoint: https://mystorageaccount001.blob.core.windows.net/
   File Endpoint: https://mystorageaccount001.file.core.windows.net/
   Table Endpoint: https://mystorageaccount001.table.core.windows.net/
   Queue Endpoint: https://mystorageaccount001.queue.core.windows.net/

Total: 1 storage account(s)
```