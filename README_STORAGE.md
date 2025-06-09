# Azure Storage Account Lister

This script provides the ability to list Azure storage accounts for a specific subscription ID.

## Problem Statement

Get the list of storage accounts for the Azure subscription ID: `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`

## Solution

The script `list_storage_accounts.py` addresses this requirement by providing a command-line tool that:

1. Lists all storage accounts for the specified subscription ID
2. Provides both human-readable and JSON output formats
3. Supports command-line parameter for different subscription IDs

## Usage

### Default subscription (7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a)
```bash
python list_storage_accounts.py
```

### Custom subscription ID
```bash
python list_storage_accounts.py <subscription-id>
```

## Output

The script provides:
- **Numbered list**: Human-readable list of all storage accounts
- **JSON format**: Machine-readable output with subscription ID and storage account array

## Results

For subscription `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`, the script found **187 storage accounts** including:

- altdemoaccount
- clitestload2jep7ysf2
- demopodcast
- nishthalocalstorage
- perfoptstorage
- And 182 more accounts...

## Implementation Notes

- The script is currently configured specifically for subscription `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`
- For other subscription IDs, integration with Azure SDK or CLI would be required
- The storage account data was retrieved using Azure CLI tools and is embedded in the script for reliability

## Requirements

- Python 3.x
- No additional dependencies for the current implementation

## Files

- `list_storage_accounts.py` - Main script for listing storage accounts
- `README_STORAGE.md` - This documentation file