# Azure Storage Account Retrieval

This script retrieves the list of storage accounts for Azure subscription `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`.

## Setup

1. Install Azure CLI and authenticate:
   ```bash
   # Install Azure CLI (if not already installed)
   curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
   
   # Login to Azure
   az login
   ```

2. Install Python dependencies:
   ```bash
   pip install -r azure_requirements.txt
   ```

## Usage

### Option 1: Azure SDK (Recommended)
```bash
python get_storage_accounts.py
```

### Option 2: Azure CLI
```bash
python get_storage_accounts_cli.py
```

### Option 3: Demo (No authentication required)
```bash
python demo_storage_accounts.py
```

The demo script shows the expected output format without requiring Azure authentication.

## Output

The script will display:
- Total number of storage accounts found
- For each storage account:
  - Name
  - Location
  - Resource Group
  - SKU type
  - Kind
  - Creation time
  - Primary blob endpoint

## Requirements

- Python 3.6+
- Azure CLI authentication
- Required Python packages (see `azure_requirements.txt`)

## Authentication

The script uses `DefaultAzureCredential` which tries multiple authentication methods in order:
1. Environment variables
2. Managed identity (if running on Azure)
3. Azure CLI credentials
4. Interactive browser authentication

Make sure you're authenticated with Azure CLI using `az login` before running the script.