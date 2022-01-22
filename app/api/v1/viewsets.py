from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from app.models import Apps
from app.api.v1.serializers import (
    AppSerializer,
)


class AppViewSet(ModelViewSet):
    serializer_class = AppSerializer
    permission_classes = (permissions.IsAuthenticated, )
    http_method_names = ["get", "post", "put", "delete"]
    queryset = Apps.objects.all()
