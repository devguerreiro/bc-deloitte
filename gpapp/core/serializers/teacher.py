from gpapp.core.models.user import User
from gpapp.core.serializers.user import UserReadSerializer, UserWriteSerializer


class TeacherReadSerializer(UserReadSerializer):
    pass


class TeacherWriteSerializer(UserWriteSerializer):
    def create(self, validated_data):
        validated_data["profile"] = User.Profile.TEACHER
        return super().create(validated_data)
