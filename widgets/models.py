from django.db import models


class Widget(models.Model):
    name = models.CharField(max_length=64)
    number_of_parts = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        ordering = ["-created_date"]
