"""
Load Test Management System for Neural Network Performance Testing

This module provides functionality to manage and organize load tests
associated with different subscription IDs, particularly for neural network
model performance evaluation.
"""

import json
from typing import Dict, List, Optional
from datetime import datetime


class LoadTest:
    """Represents a load test configuration for neural network performance testing."""
    
    def __init__(self, test_id: str, name: str, model_type: str, 
                 test_type: str = "performance", created_at: str = None):
        """
        Initialize a LoadTest instance.
        
        Args:
            test_id: Unique identifier for the test
            name: Human-readable name for the test
            model_type: Type of neural network model being tested
            test_type: Type of load test (performance, accuracy, etc.)
            created_at: ISO timestamp of test creation
        """
        self.test_id = test_id
        self.name = name
        self.model_type = model_type
        self.test_type = test_type
        self.created_at = created_at or datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """Convert LoadTest to dictionary representation."""
        return {
            'test_id': self.test_id,
            'name': self.name,
            'model_type': self.model_type,
            'test_type': self.test_type,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'LoadTest':
        """Create LoadTest from dictionary representation."""
        return cls(
            test_id=data['test_id'],
            name=data['name'],
            model_type=data['model_type'],
            test_type=data.get('test_type', 'performance'),
            created_at=data.get('created_at')
        )


class LoadTestManager:
    """Manages load tests organized by subscription IDs."""
    
    def __init__(self):
        """Initialize the LoadTestManager with default test data."""
        self._subscription_tests = self._initialize_default_tests()
    
    def _initialize_default_tests(self) -> Dict[str, List[LoadTest]]:
        """Initialize with some default test data."""
        default_tests = {}
        
        # Initialize tests for the specific subscription ID mentioned in the issue
        subscription_id = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"
        default_tests[subscription_id] = [
            LoadTest(
                test_id="lt_001",
                name="PyTorch CNN Performance Test",
                model_type="CNN",
                test_type="performance"
            ),
            LoadTest(
                test_id="lt_002", 
                name="RNN Sentiment Analysis Load Test",
                model_type="RNN",
                test_type="load"
            ),
            LoadTest(
                test_id="lt_003",
                name="Autoencoder Compression Benchmark",
                model_type="Autoencoder", 
                test_type="benchmark"
            ),
            LoadTest(
                test_id="lt_004",
                name="Seq2Seq Translation Performance",
                model_type="Seq2Seq",
                test_type="performance"
            ),
            LoadTest(
                test_id="lt_005",
                name="MNIST Classification Stress Test",
                model_type="MLP",
                test_type="stress"
            )
        ]
        
        return default_tests
    
    def get_load_tests(self, subscription_id: str) -> List[LoadTest]:
        """
        Get all load tests for a specific subscription ID.
        
        Args:
            subscription_id: The subscription ID to retrieve tests for
            
        Returns:
            List of LoadTest objects for the subscription, or empty list if none found
        """
        return self._subscription_tests.get(subscription_id, [])
    
    def get_load_tests_dict(self, subscription_id: str) -> List[Dict]:
        """
        Get all load tests for a specific subscription ID as dictionaries.
        
        Args:
            subscription_id: The subscription ID to retrieve tests for
            
        Returns:
            List of dictionaries representing LoadTest objects
        """
        tests = self.get_load_tests(subscription_id)
        return [test.to_dict() for test in tests]
    
    def add_load_test(self, subscription_id: str, load_test: LoadTest) -> bool:
        """
        Add a load test to a subscription.
        
        Args:
            subscription_id: The subscription ID to add the test to
            load_test: The LoadTest object to add
            
        Returns:
            True if test was added successfully
        """
        if subscription_id not in self._subscription_tests:
            self._subscription_tests[subscription_id] = []
        
        self._subscription_tests[subscription_id].append(load_test)
        return True
    
    def get_subscription_count(self) -> int:
        """Get the number of subscriptions with tests."""
        return len(self._subscription_tests)
    
    def get_all_subscription_ids(self) -> List[str]:
        """Get all subscription IDs that have tests."""
        return list(self._subscription_tests.keys())


# Global instance for easy access
load_test_manager = LoadTestManager()


def get_load_tests_for_subscription(subscription_id: str) -> List[Dict]:
    """
    Convenience function to get load tests for a subscription ID.
    
    Args:
        subscription_id: The subscription ID to retrieve tests for
        
    Returns:
        List of dictionaries representing load tests
    """
    return load_test_manager.get_load_tests_dict(subscription_id)


if __name__ == "__main__":
    # Example usage
    subscription_id = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"
    tests = get_load_tests_for_subscription(subscription_id)
    
    print(f"Load tests for subscription {subscription_id}:")
    for test in tests:
        print(f"  - {test['name']} ({test['model_type']}) - {test['test_type']}")