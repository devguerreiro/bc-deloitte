from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from gpapp.core.models.lesson import Lesson, LessonGrade
from gpapp.core.serializers.lesson import (
    LessonReadSerializer,
    LessonWriteSerializer,
    StudentGradeWriteSerializer,
)


class LessonViewSet(ModelViewSet):
    read_serializer = LessonReadSerializer
    write_serializer = LessonWriteSerializer
    queryset = Lesson.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return self.read_serializer
        elif self.action in ["create", "update"]:
            return self.write_serializer
        raise NotImplementedError("Serializer was not defined")

    @action(detail=True, methods=["PUT"])
    def student_grades(self, request: Request, pk=None):
        lesson = self.get_object()
        lesson_grade = get_object_or_404(LessonGrade, lesson=lesson)

        serializer = StudentGradeWriteSerializer(
            instance=lesson_grade, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)
