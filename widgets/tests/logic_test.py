from datetime import datetime
from typing import Any, Dict

import pytest

from widgets.models import Widget
from widgets.serializers import WidgetSerializer

pytestmark = pytest.mark.django_db


class TestWidgetModel:
    def test_widget_creation(self) -> None:
        """Test creating a widget through the model."""
        widget = Widget.objects.create(name="Model Test", number_of_parts=7)
        assert widget.name == "Model Test"
        assert widget.number_of_parts == 7
        assert isinstance(widget.created_date, datetime)
        assert isinstance(widget.updated_date, datetime)

    def test_widget_string_representation(self) -> None:
        """Test the string representation of a widget."""
        widget = Widget.objects.create(name="Widget Name", number_of_parts=3)
        assert str(widget) == "Widget Name"

    def test_widget_ordering(self) -> None:
        """Test that widgets are ordered by created_date in descending order."""
        Widget.objects.create(name="First Widget", number_of_parts=1)
        Widget.objects.create(name="Second Widget", number_of_parts=2)
        widgets = Widget.objects.all()
        assert widgets[0].name == "Second Widget"
        assert widgets[1].name == "First Widget"


class TestWidgetSerializer:
    def test_serializer_validation_valid_data(
        self, valid_widget_data: Dict[str, Any]
    ) -> None:
        """Test serializer validation with valid data."""
        serializer = WidgetSerializer(data=valid_widget_data)
        assert serializer.is_valid()

    def test_serializer_validation_invalid_name(self) -> None:
        """Test serializer validation with an invalid name (too long)."""
        data = {"name": "x" * 65, "number_of_parts": 5}
        serializer = WidgetSerializer(data=data)
        assert not serializer.is_valid()
        assert "name" in serializer.errors

    def test_serializer_validation_invalid_parts(self) -> None:
        """Test serializer validation with invalid number of parts (negative)."""
        data = {"name": "Valid Name", "number_of_parts": -5}
        serializer = WidgetSerializer(data=data)
        assert not serializer.is_valid()
        assert "number_of_parts" in serializer.errors

    def test_serializer_fields(self, existing_widget: Widget) -> None:
        """Test that the serializer includes all required fields."""
        serializer = WidgetSerializer(existing_widget)
        data = serializer.data
        assert "id" in data
        assert "name" in data
        assert "number_of_parts" in data
        assert "created_date" in data
        assert "updated_date" in data
