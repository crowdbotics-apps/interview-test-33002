from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from app.models import Apps, Plan, Subscription
from app.api.v1.serializers import (
    AppSerializer,
    PlanSerializer,
    SubscriptionSerializer,
)


class AppViewSet(ModelViewSet):
    serializer_class = AppSerializer
    permission_classes = (permissions.IsAuthenticated, )
    http_method_names = ["get", "post", "put", "delete"]
    queryset = Apps.objects.all()


class PlanViewSet(ModelViewSet):
    serializer_class = PlanSerializer
    permission_classes = (permissions.IsAuthenticated, )
    http_method_names = ["get"]
    queryset = Plan.objects.all()


class SubscriptionViewSet(ModelViewSet):
    serializer_class = SubscriptionSerializer
    permission_classes = (permissions.IsAuthenticated, )
    http_method_names = ["get", "post", "put"]
    queryset = Subscription.objects.all()
