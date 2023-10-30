from rest_framework import serializers

from gpapp.core.models.user import User


class UserReadSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    dob = serializers.DateField(format="%d/%m/%Y", read_only=True)
    profile = serializers.IntegerField(read_only=True)


class UserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "email",
            "password",
            "dob",
            "profile",
        ]
        read_only_fields = ["profile"]
        write_only_fields = ["password"]
        extra_kwargs = {
            "dob": {
                "format": "%d/%m/%Y",
                "input_formats": ["%d/%m/%Y"],
            }
        }

    def __init__(self, instance=None, data=..., **kwargs):
        if instance:
            data["password"] = instance.password
        super().__init__(instance, data, **kwargs)

    def create(self, validated_data):
        return User.objects.create_user(
            **validated_data, username=validated_data["email"]
        )

    def update(self, instance, validated_data):
        User.objects.filter(pk=instance.id).update(
            **validated_data, username=validated_data["email"]
        )
        return instance
