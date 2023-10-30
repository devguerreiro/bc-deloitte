import pytest


@pytest.mark.django_db
class TestStudentPermission:
    @staticmethod
    def test_should_not_be_able_to_get_student_grades(
        client,
        populate_teacher,
        populate_student,
    ):
        # given
        student = populate_student()
        teacher = populate_teacher()

        url = f"/api/v1/student/{student.id}/grades/"

        client.force_authenticate(teacher)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_list_students(
        client,
        populate_teacher,
    ):
        # given
        teacher = populate_teacher()

        url = "/api/v1/student/"

        client.force_authenticate(teacher)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_retrieve_student(
        client, populate_teacher, populate_student
    ):
        # given
        student = populate_student()
        teacher = populate_teacher()

        url = f"/api/v1/student/{student.id}/"

        client.force_authenticate(teacher)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_create_students(
        client,
        populate_teacher,
    ):
        # given
        teacher = populate_teacher()

        url = "/api/v1/student/"

        client.force_authenticate(teacher)

        # when
        response = client.post(url, data={})

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_delete_student(
        client, populate_teacher, populate_student
    ):
        # given
        student = populate_student()
        teacher = populate_teacher()

        url = f"/api/v1/student/{student.id}/"

        client.force_authenticate(teacher)

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_update_student(
        client, populate_teacher, populate_student
    ):
        # given
        student = populate_student()
        teacher = populate_teacher()

        url = f"/api/v1/student/{student.id}/"

        client.force_authenticate(teacher)

        # when
        response = client.put(url, data={})

        # assert
        assert response.status_code == 403


@pytest.mark.django_db
class TestTeacherPermission:
    @staticmethod
    def test_should_not_be_able_to_list_teachers(
        client,
        populate_teacher,
    ):
        # given
        teacher = populate_teacher()

        url = "/api/v1/teacher/"

        client.force_authenticate(teacher)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_retrieve_a_teacher(client, populate_teacher):
        # given
        teachers = populate_teacher(quantity=2)

        url = f"/api/v1/teacher/{teachers[1].id}/"

        client.force_authenticate(teachers[0])

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_be_able_to_retrieve_yourself(client, populate_teacher):
        # given
        teacher = populate_teacher()

        url = f"/api/v1/teacher/{teacher.id}/"

        client.force_authenticate(teacher)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_not_be_able_to_create_teachers(client, populate_teacher):
        # given
        teacher = populate_teacher()

        url = "/api/v1/teacher/"

        client.force_authenticate(teacher)

        # when
        response = client.post(url, data={})

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_delete_a_teacher(client, populate_teacher):
        # given
        teachers = populate_teacher(quantity=2)

        url = f"/api/v1/teacher/{teachers[1].id}/"

        client.force_authenticate(teachers[0])

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_update_a_teacher(client, populate_teacher):
        # given
        teachers = populate_teacher(quantity=2)

        url = f"/api/v1/teacher/{teachers[1].id}/"

        client.force_authenticate(teachers[0])

        # when
        response = client.put(url, data={})

        # assert
        assert response.status_code == 403


@pytest.mark.django_db
class TestCoordinatorPermission:
    @staticmethod
    def test_should_not_be_able_to_list_coordinators(
        client,
        populate_teacher,
    ):
        # given
        teacher = populate_teacher()

        url = "/api/v1/coordinator/"

        client.force_authenticate(teacher)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_retrieve_a_coordinator(
        client, populate_teacher, populate_coordinator
    ):
        # given
        coordinator = populate_coordinator()
        teacher = populate_teacher()

        url = f"/api/v1/coordinator/{coordinator.id}/"

        client.force_authenticate(teacher)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_create_coordinators(client, populate_teacher):
        # given
        teacher = populate_teacher()

        url = "/api/v1/coordinator/"

        client.force_authenticate(teacher)

        # when
        response = client.post(url, data={})

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_delete_a_coordinator(
        client, populate_teacher, populate_coordinator
    ):
        # given
        coordinator = populate_coordinator()
        teacher = populate_teacher()

        url = f"/api/v1/coordinator/{coordinator.id}/"

        client.force_authenticate(teacher)

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_update_a_coordinator(
        client, populate_teacher, populate_coordinator
    ):
        # given
        coordinator = populate_coordinator()
        teacher = populate_teacher()

        url = f"/api/v1/coordinator/{coordinator.id}/"

        client.force_authenticate(teacher)

        # when
        response = client.put(url, data={})

        # assert
        assert response.status_code == 403


@pytest.mark.django_db
class TestLessonPermission:
    @staticmethod
    def test_should_be_able_to_list_lessons(client, populate_teacher):
        # given
        teacher = populate_teacher()

        url = "/api/v1/lesson/"

        client.force_authenticate(teacher)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_not_be_able_to_retrieve_a_lesson_that_he_is_not_the_teacher(
        client, populate_teacher, populate_lesson
    ):
        # given
        teacher = populate_teacher()
        lesson = populate_lesson()

        url = f"/api/v1/lesson/{lesson.id}/"

        client.force_authenticate(teacher)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_be_able_to_retrieve_a_lesson_that_he_is_the_teacher(
        client, populate_teacher, populate_lesson
    ):
        # given
        teacher = populate_teacher()
        lesson = populate_lesson(teacher=teacher)

        url = f"/api/v1/lesson/{lesson.id}/"

        client.force_authenticate(teacher)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_not_be_able_to_create_lessons(client, populate_teacher):
        # given
        teacher = populate_teacher()

        url = "/api/v1/lesson/"

        client.force_authenticate(teacher)

        # when
        response = client.post(url, data={})

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_delete_a_lesson(
        client, populate_teacher, populate_lesson
    ):
        # given
        lesson = populate_lesson()
        teacher = populate_teacher()

        url = f"/api/v1/lesson/{lesson.id}/"

        client.force_authenticate(teacher)

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_update_a_lesson(
        client, populate_teacher, populate_lesson
    ):
        # given
        lesson = populate_lesson()
        teacher = populate_teacher()

        url = f"/api/v1/lesson/{lesson.id}/"

        client.force_authenticate(teacher)

        # when
        response = client.put(url, data={})

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_be_able_to_update_the_student_grades(
        client, populate_teacher, populate_lesson, populate_lesson_grade
    ):
        # given
        teacher = populate_teacher()
        lesson = populate_lesson(teacher=teacher)
        populate_lesson_grade(lesson=lesson)

        url = f"/api/v1/lesson/{lesson.id}/student_grades/"

        client.force_authenticate(teacher)

        # when
        response = client.put(url, data={})

        # assert
        assert response.status_code == 404
