from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from gpapp.core.models.teacher import Teacher
from gpapp.core.permissions.coordinator import CoordinatorPermission
from gpapp.core.permissions.teacher import TeacherPermission
from gpapp.core.serializers.lesson import TeacherLessonReadSerializer
from gpapp.core.serializers.teacher import TeacherReadSerializer, TeacherWriteSerializer


class TeacherViewSet(ModelViewSet):
    read_serializer = TeacherReadSerializer
    write_serializer = TeacherWriteSerializer
    queryset = Teacher.objects.all()
    permission_classes = [TeacherPermission | CoordinatorPermission | IsAdminUser]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return self.read_serializer
        elif self.action in ["create", "update"]:
            return self.write_serializer
        raise NotImplementedError("Serializer was not defined")

    @action(detail=True)
    def lessons(self, request: Request, pk: int):
        teacher = self.get_object()
        serializer = TeacherLessonReadSerializer(
            instance=teacher.lessons_as_teacher,
            many=True,
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)
