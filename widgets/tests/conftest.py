from typing import Any, Dict, Generator

import pytest
from rest_framework.test import APIClient

from widgets.models import Widget


@pytest.fixture
def api_client() -> APIClient:
    """Return an API client for testing."""
    return APIClient()


@pytest.fixture
def valid_widget_data() -> Dict[str, Any]:
    """Return valid data for creating a widget."""
    return {"name": "Test Widget", "number_of_parts": 10}


@pytest.fixture
def invalid_widget_data() -> Dict[str, Any]:
    """Return invalid data for creating a widget."""
    return {
        "name": "x" * 65,  # Exceeds 64 char limit
        "number_of_parts": -5,  # Negative value not allowed
    }


@pytest.fixture
def existing_widget() -> Generator[Widget, None, None]:
    """Create and return a widget for testing."""
    widget = Widget.objects.create(name="Existing Widget", number_of_parts=5)
    yield widget
    # Clean up if the test didn't delete it
    try:
        Widget.objects.get(pk=widget.pk).delete()
    except Widget.DoesNotExist:
        pass
