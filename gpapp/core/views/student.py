from rest_framework.viewsets import ModelViewSet

from gpapp.core.models.student import Student
from gpapp.core.serializers.student import StudentReadSerializer, StudentWriteSerializer


class StudentViewSet(ModelViewSet):
    read_serializer = StudentReadSerializer
    write_serializer = StudentWriteSerializer
    queryset = Student.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return self.read_serializer
        elif self.action in ["create", "update"]:
            return self.write_serializer
        raise NotImplementedError("Serializer was not defined")
