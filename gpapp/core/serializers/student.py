from rest_framework import serializers

from gpapp.core.models.user import User
from gpapp.core.serializers.user import UserReadSerializer, UserWriteSerializer


class StudentReadSerializer(UserReadSerializer):
    pass


class StudentWriteSerializer(UserWriteSerializer):
    def create(self, validated_data):
        validated_data["profile"] = User.Profile.STUDENT
        return super().create(validated_data)


class StudentLessonReadSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


class StudentGradeReadSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    lesson = StudentLessonReadSerializer()
    grades = serializers.JSONField(read_only=True)
