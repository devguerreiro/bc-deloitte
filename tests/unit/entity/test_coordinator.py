from gpapp.core.models.coordinator import Coordinator


class TestCoordinator:
    @staticmethod
    def test_should_has_attributes():
        assert hasattr(Coordinator, "id")
        assert hasattr(Coordinator, "name")
        assert hasattr(Coordinator, "email")
        assert hasattr(Coordinator, "dob")

    @staticmethod
    def test_should_has_repr(make_coordinator):
        # given
        coordinator = make_coordinator()

        # when
        output = repr(coordinator)

        # act
        assert output == coordinator.name

    @staticmethod
    def test_should_has_str(make_coordinator):
        # given
        coordinator = make_coordinator()

        # when
        output = str(coordinator)

        # act
        assert output == coordinator.name
