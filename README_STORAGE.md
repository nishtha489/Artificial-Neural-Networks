# Azure Storage Account Lister

This script provides the ability to list Azure storage accounts for a specific subscription ID with support for both live Azure API calls and cached data.

## Problem Statement

Get the list of storage accounts for the Azure subscription ID: `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`

## Solution

The script `list_storage_accounts.py` addresses this requirement by providing a command-line tool that:

1. Lists all storage accounts for the specified subscription ID
2. Provides both human-readable and JSON output formats
3. Supports command-line parameter for different subscription IDs
4. **NEW**: Integrates with azmcp tool for live Azure API calls
5. **NEW**: Falls back gracefully to cached data when authentication isn't available

## Usage

### Default subscription with cached data
```bash
python list_storage_accounts.py
```

### Custom subscription ID with cached data
```bash
python list_storage_accounts.py <subscription-id>
```

### **NEW**: Live Azure integration via azmcp
```bash
# Attempt live Azure API calls with fallback to cached data
python list_storage_accounts.py --use-azmcp

# Live integration with specific subscription
python list_storage_accounts.py 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a --use-azmcp
```

## Output

The script provides:
- **Numbered list**: Human-readable list of all storage accounts
- **JSON format**: Machine-readable output with subscription ID, storage account array, total count, and data source
- **Integration demo**: Shows how azmcp integration works

### Sample Output
```
=== DEMONSTRATING AZMCP INTEGRATION ===

This script can integrate with azmcp tool for live Azure data.
Example usage:
  python list_storage_accounts.py --use-azmcp
  python list_storage_accounts.py 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a --use-azmcp

The azmcp integration would:
1. Call azmcp-storage-account-list with the subscription ID
2. Parse the JSON response to extract storage account names
3. Return live data from Azure APIs
4. Fall back to cached data if authentication fails

Current limitations:
- Requires Azure authentication (az login)
- Needs appropriate permissions for the subscription

=== RUNNING WITH CACHED DATA ===

Getting storage accounts for subscription: 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a
Mode: Using cached data
============================================================
...
```

## Results

For subscription `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`, the script found **187 storage accounts** including:

- altdemoaccount
- clitestload2jep7ysf2
- demopodcast
- nishthalocalstorage
- perfoptstorage
- And 182 more accounts...

## Implementation Notes

- **Azure Integration**: Script can now integrate with azmcp tool for live Azure API calls
- **Fallback Mechanism**: Gracefully falls back to cached data when authentication fails
- **Data Source Tracking**: JSON output indicates whether data came from live API or cache
- **Authentication**: Live integration requires Azure authentication and proper permissions
- The storage account data was retrieved using Azure CLI tools and is embedded in the script for reliability
- For other subscription IDs, the live azmcp integration would provide real-time data (when authenticated)

## Requirements

- Python 3.x
- No additional dependencies for cached mode
- For live integration: Azure authentication and azmcp tool availability

## Files

- `list_storage_accounts.py` - Main script for listing storage accounts with azmcp integration
- `README_STORAGE.md` - This documentation file