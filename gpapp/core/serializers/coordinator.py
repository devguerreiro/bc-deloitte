from gpapp.core.models.user import User
from gpapp.core.serializers.user import UserReadSerializer, UserWriteSerializer


class CoordinatorReadSerializer(UserReadSerializer):
    pass


class CoordinatorWriteSerializer(UserWriteSerializer):
    def create(self, validated_data):
        validated_data["profile"] = User.Profile.COORDINATOR
        return super().create(validated_data)
