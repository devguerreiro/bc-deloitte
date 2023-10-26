from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from gpapp.core.models.student import Student
from gpapp.core.serializers.student import (
    StudentGradeReadSerializer,
    StudentReadSerializer,
    StudentWriteSerializer,
)


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

    @action(detail=True)
    def grades(self, request: Request, pk: int):
        student = self.get_object()
        serializer = StudentGradeReadSerializer(
            instance=student.grades,
            many=True,
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)
