import pytest


@pytest.mark.django_db
class TestStudentPermission:
    @staticmethod
    def test_should_be_able_to_get_student_grades(
        client,
        populate_coordinator,
        populate_student,
    ):
        # given
        student = populate_student()
        coordinator = populate_coordinator()

        url = f"/api/v1/student/{student.id}/grades/"

        client.force_authenticate(coordinator)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_be_able_to_list_students(
        client,
        populate_coordinator,
    ):
        # given
        coordinator = populate_coordinator()

        url = "/api/v1/student/"

        client.force_authenticate(coordinator)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_be_able_to_retrieve_student(
        client, populate_coordinator, populate_student
    ):
        # given
        student = populate_student()
        coordinator = populate_coordinator()

        url = f"/api/v1/student/{student.id}/"

        client.force_authenticate(coordinator)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_be_able_to_create_students(
        client,
        populate_coordinator,
    ):
        # given
        coordinator = populate_coordinator()

        url = "/api/v1/student/"

        client.force_authenticate(coordinator)

        # when
        response = client.post(url, data={})

        # assert
        assert response.status_code == 400

    @staticmethod
    def test_should_be_able_to_delete_student(
        client, populate_coordinator, populate_student
    ):
        # given
        student = populate_student()
        coordinator = populate_coordinator()

        url = f"/api/v1/student/{student.id}/"

        client.force_authenticate(coordinator)

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 204

    @staticmethod
    def test_should_be_able_to_update_student(
        client, populate_coordinator, populate_student
    ):
        # given
        student = populate_student()
        coordinator = populate_coordinator()

        url = f"/api/v1/student/{student.id}/"

        client.force_authenticate(coordinator)

        # when
        response = client.put(url, data={})

        # assert
        assert response.status_code == 400


@pytest.mark.django_db
class TestTeacherPermission:
    @staticmethod
    def test_should_be_able_to_list_teachers(
        client,
        populate_coordinator,
    ):
        # given
        coordinator = populate_coordinator()

        url = "/api/v1/teacher/"

        client.force_authenticate(coordinator)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_be_able_to_retrieve_a_teacher(
        client, populate_coordinator, populate_teacher
    ):
        # given
        coordinator = populate_coordinator()
        teacher = populate_teacher()

        url = f"/api/v1/teacher/{teacher.id}/"

        client.force_authenticate(coordinator)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_be_able_to_create_teachers(client, populate_coordinator):
        # given
        coordinator = populate_coordinator()

        url = "/api/v1/teacher/"

        client.force_authenticate(coordinator)

        # when
        response = client.post(url, data={})

        # assert
        assert response.status_code == 400

    @staticmethod
    def test_should_be_able_to_delete_a_teacher(
        client, populate_coordinator, populate_teacher
    ):
        # given
        teacher = populate_teacher()
        coordinator = populate_coordinator()

        url = f"/api/v1/teacher/{teacher.id}/"

        client.force_authenticate(coordinator)

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 204

    @staticmethod
    def test_should_be_able_to_update_a_teacher(
        client, populate_coordinator, populate_teacher
    ):
        # given
        teacher = populate_teacher()
        coordinator = populate_coordinator()

        url = f"/api/v1/teacher/{teacher.id}/"

        client.force_authenticate(coordinator)

        # when
        response = client.put(url, data={})

        # assert
        assert response.status_code == 400


@pytest.mark.django_db
class TestCoordinatorPermission:
    @staticmethod
    def test_should_not_be_able_to_list_coordinators(
        client,
        populate_coordinator,
    ):
        # given
        coordinator = populate_coordinator()

        url = "/api/v1/coordinator/"

        client.force_authenticate(coordinator)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_retrieve_a_coordinator(client, populate_coordinator):
        # given
        coordinators = populate_coordinator(quantity=2)

        url = f"/api/v1/coordinator/{coordinators[1].id}/"

        client.force_authenticate(coordinators[0])

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_create_coordinators(client, populate_coordinator):
        # given
        coordinator = populate_coordinator()

        url = "/api/v1/coordinator/"

        client.force_authenticate(coordinator)

        # when
        response = client.post(url, data={})

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_delete_a_coordinator(client, populate_coordinator):
        # given
        coordinators = populate_coordinator(quantity=2)

        url = f"/api/v1/coordinator/{coordinators[1].id}/"

        client.force_authenticate(coordinators[0])

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_update_a_coordinator(client, populate_coordinator):
        # given
        coordinators = populate_coordinator(quantity=2)

        url = f"/api/v1/coordinator/{coordinators[1].id}/"

        client.force_authenticate(coordinators[0])

        # when
        response = client.put(url, data={})

        # assert
        assert response.status_code == 403


@pytest.mark.django_db
class TestLessonPermission:
    @staticmethod
    def test_should_be_able_to_list_lessons(client, populate_coordinator):
        # given
        coordinator = populate_coordinator()

        url = "/api/v1/lesson/"

        client.force_authenticate(coordinator)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_be_able_to_retrieve_a_lesson(
        client, populate_coordinator, populate_lesson
    ):
        # given
        coordinator = populate_coordinator()
        lesson = populate_lesson()

        url = f"/api/v1/lesson/{lesson.id}/"

        client.force_authenticate(coordinator)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_be_able_to_create_lessons(client, populate_coordinator):
        # given
        coordinator = populate_coordinator()

        url = "/api/v1/lesson/"

        client.force_authenticate(coordinator)

        # when
        response = client.post(url, data={})

        # assert
        assert response.status_code == 400

    @staticmethod
    def test_should_be_able_to_delete_a_lesson(
        client, populate_coordinator, populate_lesson
    ):
        # given
        lesson = populate_lesson()
        coordinator = populate_coordinator()

        url = f"/api/v1/lesson/{lesson.id}/"

        client.force_authenticate(coordinator)

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 204

    @staticmethod
    def test_should_be_able_to_update_a_lesson(
        client, populate_coordinator, populate_lesson
    ):
        # given
        lesson = populate_lesson()
        coordinator = populate_coordinator()

        url = f"/api/v1/lesson/{lesson.id}/"

        client.force_authenticate(coordinator)

        # when
        response = client.put(url, data={})

        # assert
        assert response.status_code == 400

    @staticmethod
    def test_should_not_be_able_to_update_the_student_grades(
        client, populate_coordinator, populate_lesson, populate_lesson_grade
    ):
        # given
        coordinator = populate_coordinator()
        lesson = populate_lesson()
        populate_lesson_grade(lesson=lesson)

        url = f"/api/v1/lesson/{lesson.id}/student_grades/"

        client.force_authenticate(coordinator)

        # when
        response = client.put(url, data={})

        # assert
        assert response.status_code == 403
