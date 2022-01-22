from django.urls import path, include

from rest_framework.routers import DefaultRouter

from app.api.v1.viewsets import (
    AppViewSet,
    PlanViewSet,
    SubscriptionViewSet
)

router = DefaultRouter()
router.register("apps", AppViewSet, basename="apps")
router.register("plans", PlanViewSet, basename="plans")
router.register("subscription", SubscriptionViewSet, basename="subscription")


urlpatterns = [
    path("", include(router.urls)),
]