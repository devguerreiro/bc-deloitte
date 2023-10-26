from gpapp.core.models.teacher import Teacher


class TestTeacher:
    @staticmethod
    def test_should_has_attributes():
        assert hasattr(Teacher, "id")
        assert hasattr(Teacher, "name")
        assert hasattr(Teacher, "email")
        assert hasattr(Teacher, "password")
        assert hasattr(Teacher, "dob")
        assert hasattr(Teacher, "profile")

    @staticmethod
    def test_should_has_repr(make_teacher):
        # given
        teacher = make_teacher()

        # when
        output = repr(teacher)

        # act
        assert output == f"{teacher.profile} | {teacher.name} - {teacher.email}"

    @staticmethod
    def test_should_has_str(make_teacher):
        # given
        teacher = make_teacher()

        # when
        output = str(teacher)

        # act
        assert output == f"{teacher.profile} | {teacher.name} - {teacher.email}"
