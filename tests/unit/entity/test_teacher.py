from gpapp.core.models.teacher import Teacher


class TestTeacher:
    @staticmethod
    def test_should_has_attributes():
        assert hasattr(Teacher, "id")
        assert hasattr(Teacher, "name")
        assert hasattr(Teacher, "email")
        assert hasattr(Teacher, "dob")

    @staticmethod
    def test_should_has_repr(make_teacher):
        # given
        teacher = make_teacher()

        # when
        output = repr(teacher)

        # act
        assert output == teacher.name

    @staticmethod
    def test_should_has_str(make_teacher):
        # given
        teacher = make_teacher()

        # when
        output = str(teacher)

        # act
        assert output == teacher.name
