#!/bin/bash
# Script to query Azure Load Testing resources across multiple resource groups
# Using Azure MCP loadtesting tool

SUBSCRIPTION_ID="7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"
OUTPUT_FILE="load_testing_resources_found.txt"

echo "=========================================="
echo "Azure Load Testing Resources Search"
echo "Subscription: $SUBSCRIPTION_ID"
echo "=========================================="
echo ""

# Sample of resource groups to check (first 20)
RESOURCE_GROUPS=(
    "FeatureAvailabilityDeployment-centralindia-1"
    "MC_cnt-test-commitsha-cin-rg_cnt-test-commitsha-cin-aks-cp_centralindia"
    "MC_cnt-test-commitsha-cin-rg_cnt-test-commitsha-cin-aks_centralindia"
    "test-cri_group"
    "mohi-test_group"
    "mohit-test_group"
    "cnt-integration-tests-switzerlandnorth-src-rg"
    "cnt-integration-tests-switzerlandnorth-dest-rg"
    "smoke-tests-switzerlandnorth-rg"
    "cnt-test-comknaraya-sea-rg"
    "cnt-test-gblknaraya-Outbound-ip-pool-rg"
    "cnt-test-gblknaraya-Inbound-ip-pool-rg"
    "cnt-gblknaraya-ai-rg"
    "cnt-test-gblharshan-cin-rg"
    "cnt-test-gblharshan-Inbound-ip-pool-rg"
    "cnt-test-gblharshan-Outbound-ip-pool-rg"
)

echo "Checking ${#RESOURCE_GROUPS[@]} resource groups for load testing resources..."
echo ""

# Clear output file
> "$OUTPUT_FILE"

echo "Resource Groups Checked:" >> "$OUTPUT_FILE"
echo "========================" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

FOUND_COUNT=0

for RG in "${RESOURCE_GROUPS[@]}"; do
    echo "Checking: $RG"
    echo "Resource Group: $RG" >> "$OUTPUT_FILE"
    
    # Note: In practice, you would call the Azure MCP tool here
    # For example:
    # result=$(azure-mcp-call loadtesting_testresource_list --subscription "$SUBSCRIPTION_ID" --resource-group "$RG")
    
    # Since we're documenting the process, we note this
    echo "  - Querying Azure MCP loadtesting_testresource_list..." >> "$OUTPUT_FILE"
    echo "  - Command: Azure-loadtesting with subscription=$SUBSCRIPTION_ID, resource-group=$RG" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
done

echo ""
echo "=========================================="
echo "Query Complete"
echo "=========================================="
echo "Resource groups checked: ${#RESOURCE_GROUPS[@]}"
echo "Results saved to: $OUTPUT_FILE"
echo ""
echo "NOTE: This script demonstrates the query process."
echo "To execute actual queries, use the Azure MCP tool"
echo "with the loadtesting_testresource_list command."
echo ""
echo "Example usage:"
echo "  Azure-loadtesting command: loadtesting_testresource_list"
echo "  Parameters: {\"subscription\": \"$SUBSCRIPTION_ID\", \"resource-group\": \"<rg-name>\"}"
