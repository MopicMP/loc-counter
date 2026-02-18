"""Tests for loc-counter."""

import pytest
from loc_counter import counter


class TestCounter:
    """Test suite for counter."""

    def test_basic(self):
        """Test basic usage."""
        result = counter("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            counter("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = counter(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
