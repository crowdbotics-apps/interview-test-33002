from django.urls import path, include

from rest_framework.routers import DefaultRouter

from app.api.v1.viewsets import (
    AppViewSet
)

router = DefaultRouter()
router.register("", AppViewSet, basename="app")


urlpatterns = [
    path("", include(router.urls)),
]