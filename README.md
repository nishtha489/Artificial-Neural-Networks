# Artificial-Neural-Networks

This repository contains various neural network implementations and assignments.

## Azure Storage Account Retrieval

Added functionality to retrieve Azure storage accounts for subscription `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`.

### Files:
- `get_storage_accounts.py` - Main script using Azure SDK
- `get_storage_accounts_cli.py` - Alternative script using Azure CLI
- `demo_storage_accounts.py` - Demo script showing expected output format
- `azure_requirements.txt` - Python dependencies for Azure SDK
- `AZURE_STORAGE_README.md` - Detailed usage instructions

### Quick Usage:
```bash
# Option 1: Using Azure SDK
pip install -r azure_requirements.txt
az login
python get_storage_accounts.py

# Option 2: Using Azure CLI
az login
python get_storage_accounts_cli.py

# Option 3: Demo (no authentication required)
python demo_storage_accounts.py
```