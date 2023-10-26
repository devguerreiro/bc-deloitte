from rest_framework.serializers import ModelSerializer

from gpapp.core.models.user import User


class UserWriteSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password", "profile"]

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["email"],
            **validated_data,
        )
