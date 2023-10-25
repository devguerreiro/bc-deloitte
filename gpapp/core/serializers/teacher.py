from rest_framework import serializers

from gpapp.core.models.teacher import Teacher


class TeacherReadSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    dob = serializers.DateField(format="%d/%m/%Y", read_only=True)


class TeacherWriteSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(input_formats=["%d/%m/%Y"])

    class Meta:
        model = Teacher
        fields = ["name", "email", "dob"]
