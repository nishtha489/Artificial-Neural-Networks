#!/usr/bin/env python3
"""
Command-line interface for Load Test Manager

Usage:
    python get_load_tests.py [subscription_id]
    
If no subscription_id is provided, it will use the default one from the issue:
7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a
"""

import sys
import json
from load_test_manager import get_load_tests_for_subscription


def main():
    """Main function to handle command line interface."""
    
    # Default subscription ID from the issue
    default_subscription_id = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"
    
    if len(sys.argv) > 1:
        subscription_id = sys.argv[1]
    else:
        subscription_id = default_subscription_id
        print(f"Using default subscription ID: {subscription_id}")
        print("To use a different subscription ID, run: python get_load_tests.py <subscription_id>")
        print()
    
    # Get the load tests
    tests = get_load_tests_for_subscription(subscription_id)
    
    if not tests:
        print(f"No load tests found for subscription ID: {subscription_id}")
        return
    
    # Display results
    print(f"Load tests for subscription {subscription_id}:")
    print(f"Total tests found: {len(tests)}")
    print("-" * 60)
    
    for i, test in enumerate(tests, 1):
        print(f"{i}. {test['name']}")
        print(f"   ID: {test['test_id']}")
        print(f"   Model Type: {test['model_type']}")
        print(f"   Test Type: {test['test_type']}")
        print(f"   Created: {test['created_at']}")
        print()
    
    # Also output as JSON for programmatic use
    if len(sys.argv) > 2 and sys.argv[2] == "--json":
        print("JSON Output:")
        print(json.dumps(tests, indent=2))


if __name__ == "__main__":
    main()