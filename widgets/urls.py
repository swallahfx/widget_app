from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import WidgetViewSet

router = DefaultRouter()
router.register(r"widgets", WidgetViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
