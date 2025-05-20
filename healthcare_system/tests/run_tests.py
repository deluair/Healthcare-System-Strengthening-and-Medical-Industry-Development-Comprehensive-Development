"""
Test runner script for the healthcare system simulation.
"""

import pytest
import sys
import os

def main():
    """Run the test suite."""
    # Add the project root to the Python path
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, project_root)
    
    # Run the tests
    pytest.main([
        "-v",  # Verbose output
        "--cov=healthcare_system",  # Enable coverage reporting
        "--cov-report=term-missing",  # Show missing lines in coverage report
        "--cov-report=html",  # Generate HTML coverage report
        "healthcare_system/tests"  # Test directory
    ])

if __name__ == "__main__":
    main() 