from rest_framework import serializers

from gpapp.core.models.lesson import Lesson, LessonGrade
from gpapp.core.models.student import Student
from gpapp.core.serializers.student import StudentReadSerializer


class LessonGradeReadSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    student = StudentReadSerializer()
    grades = serializers.JSONField(read_only=True)


class LessonGradeWriteSerializer(serializers.Serializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    grades = serializers.JSONField()


class LessonReadSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    teachers_name = serializers.CharField(read_only=True)
    load = serializers.IntegerField(read_only=True)
    students = LessonGradeReadSerializer(many=True)


class LessonWriteSerializer(serializers.ModelSerializer):
    students = LessonGradeWriteSerializer(
        many=True,
        write_only=True,
        required=False,
    )

    class Meta:
        model = Lesson
        fields = ["name", "teachers_name", "load", "students"]

    def create(self, validated_data):
        students = validated_data.pop("students", [])
        lesson = Lesson.objects.create(**validated_data)
        if students:
            LessonGrade.objects.bulk_create(
                [LessonGrade(lesson=lesson, **student) for student in students]
            )
        return lesson

    def update(self, instance, validated_data):
        students = validated_data.pop("students", [])
        Lesson.objects.filter(id=instance.id).update(**validated_data)
        for student in students:
            LessonGrade.objects.update_or_create(
                lesson=instance, **student, defaults=student
            )
        return instance