from rest_framework import serializers

from gpapp.core.models.coordinator import Coordinator


class CoordinatorReadSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    dob = serializers.DateField(format="%d/%m/%Y", read_only=True)


class CoordinatorWriteSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(input_formats=["%d/%m/%Y"])

    class Meta:
        model = Coordinator
        fields = ["name", "email", "dob"]
