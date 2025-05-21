import json
from typing import Any, Dict

import pytest
from django.urls import reverse
from rest_framework import status

from widgets.models import Widget

pytestmark = pytest.mark.django_db


class TestWidgetEndpoints:
    def test_create_valid_widget(
        self, api_client: Any, valid_widget_data: Dict[str, Any]
    ) -> None:
        """Test creating a valid widget via the API endpoint."""
        response = api_client.post(
            reverse("widget-list"),
            data=json.dumps(valid_widget_data),
            content_type="application/json",
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert Widget.objects.count() == 1

    def test_create_invalid_widget(
        self, api_client: Any, invalid_widget_data: Dict[str, Any]
    ) -> None:
        """Test creating an invalid widget via the API endpoint."""
        response = api_client.post(
            reverse("widget-list"),
            data=json.dumps(invalid_widget_data),
            content_type="application/json",
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_get_widget_list(self, api_client: Any, existing_widget: Widget) -> None:
        """Test retrieving a list of widgets via the API endpoint."""
        response = api_client.get(reverse("widget-list"))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1

    def test_get_widget_detail(self, api_client: Any, existing_widget: Widget) -> None:
        """Test retrieving a single widget via the API endpoint."""
        response = api_client.get(
            reverse("widget-detail", kwargs={"pk": existing_widget.id})
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == "Existing Widget"

    def test_update_widget(self, api_client: Any, existing_widget: Widget) -> None:
        """Test updating a widget via the API endpoint."""
        update_data = {"name": "Updated Widget", "number_of_parts": 15}
        response = api_client.put(
            reverse("widget-detail", kwargs={"pk": existing_widget.id}),
            data=json.dumps(update_data),
            content_type="application/json",
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == "Updated Widget"
        assert response.data["number_of_parts"] == 15

    def test_delete_widget(self, api_client: Any, existing_widget: Widget) -> None:
        """Test deleting a widget via the API endpoint."""
        response = api_client.delete(
            reverse("widget-detail", kwargs={"pk": existing_widget.id})
        )
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Widget.objects.count() == 0
