from django.urls import path, include

from rest_framework.routers import DefaultRouter

from app.api.v1.viewsets import (
    AppViewSet,
    PlanViewSet
)

router = DefaultRouter()
router.register("apps", AppViewSet, basename="apps")
router.register("plans", PlanViewSet, basename="plans")


urlpatterns = [
    path("", include(router.urls)),
]