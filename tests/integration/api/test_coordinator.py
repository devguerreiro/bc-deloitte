import pytest

from gpapp.core.models.coordinator import Coordinator
from gpapp.core.models.user import User


@pytest.mark.django_db
class TestCoordinator:
    @staticmethod
    def test_should_be_able_to_list_coordinators(admin_client, populate_coordinator):
        # given
        populate_coordinator(quantity=3)

        url = "/api/v1/coordinator/"

        # when
        response = admin_client.get(url)

        # assert
        assert response.status_code == 200

        assert len(response.data) == 3

        assert response.data[0].get("id") is not None
        assert response.data[0].get("name") is not None
        assert response.data[0].get("email") is not None
        assert response.data[0].get("dob") is not None
        assert response.data[0].get("profile") is not None
        assert response.data[0].get("password") is None

    @staticmethod
    def test_should_be_able_to_retrieve_an_coordinator(
        admin_client, populate_coordinator
    ):
        # given
        coordinator = populate_coordinator()

        url = f"/api/v1/coordinator/{coordinator.id}/"

        # when
        response = admin_client.get(url)

        # assert
        assert response.status_code == 200

        assert response.data["id"] == coordinator.id
        assert response.data["name"] == coordinator.name
        assert response.data["email"] == coordinator.email
        assert response.data["dob"] == coordinator.dob.strftime("%d/%m/%Y")
        assert response.data["profile"] == User.Profile.COORDINATOR
        assert response.data.get("password") is None

    @staticmethod
    def test_should_be_able_to_delete_an_coordinator(
        admin_client, populate_coordinator
    ):
        # given
        coordinator = populate_coordinator()

        url = f"/api/v1/coordinator/{coordinator.id}/"

        # when
        response = admin_client.delete(url)

        # assert
        assert response.status_code == 204

        assert Coordinator.objects.count() == 0

    @staticmethod
    def test_should_be_able_to_create_an_coordinator(admin_client, make_coordinator):
        # given
        coordinator = make_coordinator()

        url = "/api/v1/coordinator/"

        data = {
            "name": coordinator.name,
            "email": coordinator.email,
            "dob": coordinator.dob.strftime("%d/%m/%Y"),
            "password": coordinator.password,
            "profile": User.Profile.COORDINATOR,
        }

        # when
        response = admin_client.post(url, data)

        # assert
        assert response.status_code == 201

        assert Coordinator.objects.count() == 1

    @staticmethod
    def test_should_be_able_to_update_an_coordinator(
        admin_client, populate_coordinator
    ):
        # given
        coordinator = populate_coordinator()

        url = f"/api/v1/coordinator/{coordinator.id}/"

        data = {
            "name": "ze da manga",
            "email": "ze@damanga.com",
            "dob": "25/10/1980",
        }

        # when
        response = admin_client.put(url, data)

        # assert
        assert response.status_code == 200

        coordinator = Coordinator.objects.get(pk=coordinator.id)
        assert coordinator.name == data["name"]
        assert coordinator.email == data["email"]
        assert coordinator.dob.strftime("%d/%m/%Y") == data["dob"]
