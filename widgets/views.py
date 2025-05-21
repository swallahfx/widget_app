from typing import Any

from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Widget
from .serializers import WidgetSerializer


class WidgetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows widgets to be viewed or edited.
    """

    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer

    def create(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """Create a new widget."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def list(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """List all widgets."""
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """Retrieve a widget by ID."""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """Update a widget."""
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """Delete a widget."""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
