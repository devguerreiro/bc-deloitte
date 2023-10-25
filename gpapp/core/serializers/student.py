from rest_framework import serializers

from gpapp.core.models.student import Student


class StudentReadSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    dob = serializers.DateField(format="%d/%m/%Y", read_only=True)


class StudentWriteSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(input_formats=["%d/%m/%Y"])

    class Meta:
        model = Student
        fields = ["name", "email", "dob"]
