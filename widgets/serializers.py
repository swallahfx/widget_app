from rest_framework import serializers

from .models import Widget


class WidgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Widget
        fields = ["id", "name", "number_of_parts", "created_date", "updated_date"]
        read_only_fields = ["created_date", "updated_date"]

    def validate_name(self, value: str) -> str:
        """Validate that name is a utf8 string and does not exceed 64 characters."""
        if len(value) > 64:
            raise serializers.ValidationError("Name cannot exceed 64 characters.")
        return value

    def validate_number_of_parts(self, value: int) -> int:
        """Validate that number_of_parts is a positive integer."""
        if value < 0:
            raise serializers.ValidationError(
                "Number of parts must be a positive integer."
            )
        return value
