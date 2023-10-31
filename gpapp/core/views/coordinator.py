from rest_framework.viewsets import ModelViewSet

from gpapp.core.models.coordinator import Coordinator
from gpapp.core.serializers.coordinator import (
    CoordinatorReadSerializer,
    CoordinatorWriteSerializer,
)


class CoordinatorViewSet(ModelViewSet):
    read_serializer = CoordinatorReadSerializer
    write_serializer = CoordinatorWriteSerializer
    queryset = Coordinator.objects.all()
    http_method_names = ["get", "post", "put", "delete"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return self.read_serializer
        elif self.action in ["create", "update"]:
            return self.write_serializer
        raise NotImplementedError("Serializer was not defined")
