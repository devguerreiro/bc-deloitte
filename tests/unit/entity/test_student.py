from gpapp.core.models.student import Student


class TestStudent:
    @staticmethod
    def test_should_has_attributes():
        assert hasattr(Student, "id")
        assert hasattr(Student, "name")
        assert hasattr(Student, "email")
        assert hasattr(Student, "password")
        assert hasattr(Student, "dob")
        assert hasattr(Student, "profile")

    @staticmethod
    def test_should_has_repr(make_student):
        # given
        student = make_student()

        # when
        output = repr(student)

        # act
        assert output == f"{student.profile} | {student.name} - {student.email}"

    @staticmethod
    def test_should_has_str(make_student):
        # given
        student = make_student()

        # when
        output = str(student)

        # act
        assert output == f"{student.profile} | {student.name} - {student.email}"
