from rest_framework import serializers

from gpapp.core.serializers.user import UserReadSerializer, UserWriteSerializer


class StudentReadSerializer(UserReadSerializer):
    pass


class StudentWriteSerializer(UserWriteSerializer):
    pass


class StudentLessonReadSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    teachers_name = serializers.CharField(read_only=True)
    load = serializers.IntegerField(read_only=True)


class StudentGradeReadSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    lesson = StudentLessonReadSerializer()
    grades = serializers.JSONField(read_only=True)
