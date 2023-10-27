from gpapp.core.models.lesson import Lesson, LessonGrade


class TestLesson:
    @staticmethod
    def test_should_has_attributes():
        assert hasattr(Lesson, "id")
        assert hasattr(Lesson, "name")
        assert hasattr(Lesson, "teacher")
        assert hasattr(Lesson, "load")
        assert hasattr(Lesson, "students")

    @staticmethod
    def test_should_has_repr(make_lesson):
        # given
        lesson = make_lesson()

        # when
        output = repr(lesson)

        # act
        assert output == lesson.name

    @staticmethod
    def test_should_has_str(make_lesson):
        # given
        lesson = make_lesson()

        # when
        output = str(lesson)

        # act
        assert output == lesson.name


class TestLessonGrade:
    @staticmethod
    def test_should_has_attributes():
        assert hasattr(LessonGrade, "id")
        assert hasattr(LessonGrade, "lesson")
        assert hasattr(LessonGrade, "student")
        assert hasattr(LessonGrade, "grades")

    @staticmethod
    def test_should_has_repr(make_lesson_grade):
        # given
        lesson_grade = make_lesson_grade()

        # when
        output = repr(lesson_grade)

        # act
        assert (
            output
            == f"{lesson_grade.lesson.name} - {lesson_grade.student.name} | {lesson_grade.grades}"  # noqa
        )

    @staticmethod
    def test_should_has_str(make_lesson_grade):
        # given
        lesson_grade = make_lesson_grade()

        # when
        output = str(lesson_grade)

        # act
        assert (
            output
            == f"{lesson_grade.lesson.name} - {lesson_grade.student.name} | {lesson_grade.grades}"  # noqa
        )
