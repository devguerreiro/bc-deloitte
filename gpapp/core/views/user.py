from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from gpapp.core.serializers.user import UserWriteSerializer


class UserViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = UserWriteSerializer
    permission_classes = []
    authentication_classes = []
