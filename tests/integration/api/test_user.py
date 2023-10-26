import pytest
from django.contrib.auth import get_user_model

from gpapp.core.models.user import User


@pytest.mark.django_db
class TestUser:
    @staticmethod
    def test_should_be_able_to_create_a_user(client):
        # given
        data = {
            "name": "ze da manga",
            "email": "ze@damanga.com",
            "password": "ainzedamanga",
            "dob": "26/10/1980",
        }

        # when
        response = client.post("/api/v1/user/", data)

        # assert
        assert response.status_code == 201

        assert get_user_model().objects.count() == 1

        user = get_user_model().objects.first()
        assert user.username == data["email"]
        assert user.profile == User.Profile.STUDENT
        assert user.password != data["password"]

    @staticmethod
    def test_should_be_able_to_create_a_user_with_profile(client):
        # given
        data = {
            "name": "ze da manga",
            "email": "ze@damanga.com",
            "password": "ainzedamanga",
            "dob": "26/10/1980",
            "profile": User.Profile.TEACHER,
        }

        # when
        response = client.post("/api/v1/user/", data)

        # assert
        assert response.status_code == 201

        assert get_user_model().objects.count() == 1

        user = get_user_model().objects.first()
        assert user.profile == User.Profile.TEACHER
