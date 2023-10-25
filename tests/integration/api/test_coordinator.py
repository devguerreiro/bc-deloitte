import pytest

from gpapp.core.models.coordinator import Coordinator


@pytest.mark.django_db
class TestCoordinatorr:
    @staticmethod
    def test_should_be_able_to_list_coordinators(client, populate_coordinator):
        # given
        populate_coordinator(3)

        url = "/api/v1/coordinator/"

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200
        assert len(response.data) == 3

    @staticmethod
    def test_should_be_able_to_retrieve_an_coordinator(client, populate_coordinator):
        # given
        coordinator = populate_coordinator(1)[0]

        url = f"/api/v1/coordinator/{coordinator.id}/"

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200
        assert response.data["id"] == str(coordinator.id)
        assert response.data["name"] == coordinator.name
        assert response.data["email"] == coordinator.email
        assert response.data["dob"] == coordinator.dob.strftime("%d/%m/%Y")

    @staticmethod
    def test_should_be_able_to_delete_an_coordinator(client, populate_coordinator):
        # given
        coordinator = populate_coordinator(1)[0]

        url = f"/api/v1/coordinator/{coordinator.id}/"

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 204
        assert Coordinator.objects.count() == 0

    @staticmethod
    def test_should_be_able_to_create_an_coordinator(client, make_coordinator):
        # given
        coordinator = make_coordinator()

        url = "/api/v1/coordinator/"

        data = {
            "name": coordinator.name,
            "email": coordinator.email,
            "dob": coordinator.dob.strftime("%d/%m/%Y"),
        }

        # when
        response = client.post(url, data)

        # assert
        assert response.status_code == 201
        assert Coordinator.objects.count() == 1

    @staticmethod
    def test_should_be_able_to_update_an_coordinator(client, populate_coordinator):
        # given
        coordinator = populate_coordinator(1)[0]

        url = f"/api/v1/coordinator/{coordinator.id}/"

        data = {
            "name": "ze da manga",
            "email": "ze@damanga.com",
            "dob": "25/10/1980",
        }

        # when
        response = client.put(url, data, content_type="application/json")

        # assert
        assert response.status_code == 200

        coordinator = Coordinator.objects.get(pk=coordinator.id)
        assert coordinator.name == data["name"]
        assert coordinator.email == data["email"]
        assert coordinator.dob.strftime("%d/%m/%Y") == data["dob"]
