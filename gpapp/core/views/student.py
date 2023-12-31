from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from gpapp.core.models.student import Student
from gpapp.core.permissions.coordinator import CoordinatorPermission
from gpapp.core.permissions.student import StudentPermission
from gpapp.core.serializers.student import (
    StudentGradeReadSerializer,
    StudentReadSerializer,
    StudentWriteSerializer,
)


class StudentViewSet(ModelViewSet):
    read_serializer = StudentReadSerializer
    write_serializer = StudentWriteSerializer
    queryset = Student.objects.all()
    permission_classes = [StudentPermission | CoordinatorPermission | IsAdminUser]
    http_method_names = ["get", "post", "put", "delete"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return self.read_serializer
        elif self.action in ["create", "update"]:
            return self.write_serializer
        raise NotImplementedError("Serializer was not defined")

    @extend_schema(
        responses=[StudentGradeReadSerializer],
        examples=[
            OpenApiExample(
                name="exemplo",
                response_only=True,
                value=[
                    {
                        "id": 1,
                        "lesson": {
                            "id": 1,
                            "name": "Foo",
                        },
                        "grades": [10, 10, 10, 10],
                    }
                ],
            ),
        ],
    )
    @action(detail=True)
    def grades(self, request: Request, pk: int):
        student = self.get_object()
        serializer = StudentGradeReadSerializer(
            instance=student.grades,
            many=True,
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)
