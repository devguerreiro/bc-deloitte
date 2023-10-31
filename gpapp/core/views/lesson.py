from django.shortcuts import get_object_or_404
from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from gpapp.core.models.lesson import Lesson, LessonGrade
from gpapp.core.permissions.coordinator import CoordinatorPermission
from gpapp.core.permissions.teacher import TeacherPermission
from gpapp.core.serializers.lesson import (
    LessonReadSerializer,
    LessonWriteSerializer,
    StudentGradeWriteSerializer,
)


class LessonViewSet(ModelViewSet):
    read_serializer = LessonReadSerializer
    write_serializer = LessonWriteSerializer
    queryset = Lesson.objects.all()
    permission_classes = [TeacherPermission | CoordinatorPermission | IsAdminUser]
    http_method_names = ["get", "post", "put", "delete"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return self.read_serializer
        elif self.action in ["create", "update"]:
            return self.write_serializer
        raise NotImplementedError("Serializer was not defined")

    @extend_schema(
        request=StudentGradeWriteSerializer,
        responses=[],
        examples=[
            OpenApiExample(
                name="exemplo",
                request_only=True,
                value={
                    "student": 1,
                    "grades": [10, 10, 10, 10],
                },
            ),
            OpenApiExample(
                name="exemplo",
                response_only=True,
                value={
                    "id": 1,
                    "lesson": 1,
                    "student": 1,
                    "grades": [10, 10, 10, 10],
                },
            ),
        ],
    )
    @action(detail=True, methods=["PUT"])
    def student_grades(self, request: Request, pk=None):
        lesson = self.get_object()
        student = request.data.get("student")
        lesson_grade = get_object_or_404(
            LessonGrade,
            lesson=lesson,
            student_id=student,
        )

        serializer = StudentGradeWriteSerializer(
            instance=lesson_grade, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)
