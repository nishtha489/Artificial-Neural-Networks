#!/usr/bin/env python3
"""
Script to list Azure Load Tests for a specified subscription ID.

This script uses Azure CLI to retrieve load tests from Azure Load Testing service.
"""

import subprocess
import json
import sys
import argparse

__version__ = "1.0.0"


def run_azure_cli_command(command):
    """
    Execute an Azure CLI command and return the output.
    
    Args:
        command: List of command arguments
        
    Returns:
        Parsed JSON output from the command
    """
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(result.stdout) if result.stdout else []
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}", file=sys.stderr)
        print(f"stderr: {e.stderr}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON output: {e}", file=sys.stderr)
        sys.exit(1)


def list_load_tests(subscription_id):
    """
    List all Azure Load Tests for the specified subscription.
    
    Args:
        subscription_id: Azure subscription ID
        
    Returns:
        List of load test resources
    """
    print(f"Fetching load tests for subscription: {subscription_id}")
    print("-" * 80)
    
    # Set the subscription context
    subprocess.run(
        ["az", "account", "set", "--subscription", subscription_id],
        check=True,
        capture_output=True
    )
    
    # List all load testing resources in the subscription
    command = [
        "az", "resource", "list",
        "--resource-type", "Microsoft.LoadTestService/loadtests",
        "--subscription", subscription_id,
        "--output", "json"
    ]
    
    load_tests = run_azure_cli_command(command)
    
    if not load_tests:
        print("No load tests found in this subscription.")
        return []
    
    print(f"Found {len(load_tests)} load test resource(s):\n")
    
    for idx, test in enumerate(load_tests, 1):
        print(f"{idx}. Load Test Resource:")
        print(f"   Name: {test.get('name', 'N/A')}")
        print(f"   Resource Group: {test.get('resourceGroup', 'N/A')}")
        print(f"   Location: {test.get('location', 'N/A')}")
        print(f"   ID: {test.get('id', 'N/A')}")
        print(f"   Type: {test.get('type', 'N/A')}")
        print()
    
    return load_tests


def main():
    """Main function to parse arguments and list load tests."""
    parser = argparse.ArgumentParser(
        description="List Azure Load Tests for a subscription"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="Show program version and exit"
    )
    parser.add_argument(
        "--subscription-id",
        default="7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a",
        help="Azure subscription ID (default: 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a)"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results in JSON format"
    )
    
    args = parser.parse_args()
    
    load_tests = list_load_tests(args.subscription_id)
    
    if args.json:
        print(json.dumps(load_tests, indent=2))


if __name__ == "__main__":
    main()
