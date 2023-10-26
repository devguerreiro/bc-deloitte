from rest_framework.viewsets import ModelViewSet

from gpapp.core.models.lesson import Lesson
from gpapp.core.serializers.lesson import LessonReadSerializer, LessonWriteSerializer


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
