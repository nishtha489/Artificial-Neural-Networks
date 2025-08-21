"""
Simple test for the load test manager functionality.
"""

import sys
sys.path.append('.')

from load_test_manager import LoadTestManager, LoadTest, get_load_tests_for_subscription


def test_load_test_manager():
    """Test the LoadTestManager functionality."""
    
    # Test the specific subscription ID from the issue
    subscription_id = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"
    
    print("Testing LoadTestManager...")
    
    # Test 1: Get tests for the subscription ID
    tests = get_load_tests_for_subscription(subscription_id)
    print(f"✓ Found {len(tests)} tests for subscription {subscription_id}")
    
    # Test 2: Verify test data structure
    if tests:
        first_test = tests[0]
        required_fields = ['test_id', 'name', 'model_type', 'test_type', 'created_at']
        for field in required_fields:
            assert field in first_test, f"Missing field: {field}"
        print("✓ Test data structure is correct")
    
    # Test 3: Test LoadTestManager directly
    manager = LoadTestManager()
    direct_tests = manager.get_load_tests(subscription_id)
    print(f"✓ Direct manager access returned {len(direct_tests)} tests")
    
    # Test 4: Test adding a new test
    new_test = LoadTest(
        test_id="test_new",
        name="Test New Load Test",
        model_type="TestModel",
        test_type="unit_test"
    )
    manager.add_load_test(subscription_id, new_test)
    updated_tests = manager.get_load_tests(subscription_id)
    print(f"✓ Successfully added test. Total tests: {len(updated_tests)}")
    
    # Test 5: Test subscription management
    subscription_count = manager.get_subscription_count()
    all_ids = manager.get_all_subscription_ids()
    print(f"✓ Manager tracking {subscription_count} subscriptions")
    print(f"✓ Subscription IDs: {all_ids}")
    
    # Test 6: Test non-existent subscription
    empty_tests = get_load_tests_for_subscription("non-existent-id")
    assert len(empty_tests) == 0, "Should return empty list for non-existent subscription"
    print("✓ Non-existent subscription returns empty list")
    
    print("\nAll tests passed! ✓")
    
    # Display the tests for the requested subscription
    print(f"\nLoad tests for subscription {subscription_id}:")
    for i, test in enumerate(tests, 1):
        print(f"{i}. {test['name']}")
        print(f"   - Model Type: {test['model_type']}")
        print(f"   - Test Type: {test['test_type']}")
        print(f"   - Test ID: {test['test_id']}")
        print(f"   - Created: {test['created_at']}")
        print()


if __name__ == "__main__":
    test_load_test_manager()