import pytest


@pytest.mark.django_db
class TestStudentPermission:
    @staticmethod
    def test_should_be_able_to_get_their_own_grades(
        client,
        populate_student,
    ):
        # given
        student = populate_student()

        url = f"/api/v1/student/{student.id}/grades/"

        client.force_authenticate(student)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_not_be_able_to_get_other_student_grades(
        client,
        populate_student,
    ):
        # given
        students = populate_student(quantity=2)

        current_student = students[0]
        other_student = students[1]

        url = f"/api/v1/student/{other_student.id}/grades/"

        client.force_authenticate(current_student)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_list_students(
        client,
        populate_student,
    ):
        # given
        student = populate_student()

        url = "/api/v1/student/"

        client.force_authenticate(student)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_be_able_to_retrieve_yourself(
        client,
        populate_student,
    ):
        # given
        student = populate_student()

        url = f"/api/v1/student/{student.id}/"

        client.force_authenticate(student)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_not_be_able_to_retrieve_other_student(
        client,
        populate_student,
    ):
        # given
        students = populate_student(quantity=2)

        current_student = students[0]
        other_student = students[1]

        url = f"/api/v1/student/{other_student.id}/"

        client.force_authenticate(current_student)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_create_students(
        client,
        populate_student,
    ):
        # given
        student = populate_student()

        url = "/api/v1/student/"

        client.force_authenticate(student)

        # when
        response = client.post(url, data={})

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_delete_other_student(
        client,
        populate_student,
    ):
        # given
        students = populate_student(quantity=2)

        current_student = students[0]
        other_student = students[1]

        url = f"/api/v1/student/{other_student.id}/"

        client.force_authenticate(current_student)

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_delete_yourself(
        client,
        populate_student,
    ):
        # given
        student = populate_student()

        url = f"/api/v1/student/{student.id}/"

        client.force_authenticate(student)

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_update_other_student(
        client,
        populate_student,
    ):
        # given
        students = populate_student(quantity=2)

        current_student = students[0]
        other_student = students[1]

        url = f"/api/v1/student/{other_student.id}/"

        client.force_authenticate(current_student)

        # when
        response = client.put(url, data={})

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_be_able_to_update_yourself(
        client,
        populate_student,
    ):
        # given
        student = populate_student()

        url = f"/api/v1/student/{student.id}/"

        client.force_authenticate(student)

        # when
        response = client.put(url, data={})

        # assert
        assert response.status_code == 400


@pytest.mark.django_db
class TestTeacherPermission:
    @staticmethod
    def test_should_not_be_able_to_list_teachers(
        client,
        populate_student,
    ):
        # given
        student = populate_student()

        url = "/api/v1/teacher/"

        client.force_authenticate(student)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_retrieve_a_teacher(
        client, populate_student, populate_teacher
    ):
        # given
        student = populate_student()
        teacher = populate_teacher()

        url = f"/api/v1/teacher/{teacher.id}/"

        client.force_authenticate(student)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_create_teachers(
        client,
        populate_student,
    ):
        # given
        student = populate_student()

        url = "/api/v1/teacher/"

        client.force_authenticate(student)

        # when
        response = client.post(url, data={})

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_delete_a_teacher(
        client, populate_student, populate_teacher
    ):
        # given
        student = populate_student()
        teacher = populate_teacher()

        url = f"/api/v1/teacher/{teacher.id}/"

        client.force_authenticate(student)

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_update_a_teacher(
        client,
        populate_student,
        populate_teacher,
    ):
        # given
        student = populate_student()
        teacher = populate_teacher()

        url = f"/api/v1/teacher/{teacher.id}/"

        client.force_authenticate(student)

        # when
        response = client.put(url, data={})

        # assert
        assert response.status_code == 403


@pytest.mark.django_db
class TestCoordinatorPermission:
    @staticmethod
    def test_should_not_be_able_to_list_coordinators(
        client,
        populate_student,
    ):
        # given
        student = populate_student()

        url = "/api/v1/coordinator/"

        client.force_authenticate(student)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_retrieve_a_coordinator(
        client, populate_student, populate_coordinator
    ):
        # given
        student = populate_student()
        coordinator = populate_coordinator()

        url = f"/api/v1/coordinator/{coordinator.id}/"

        client.force_authenticate(student)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_create_coordinators(
        client,
        populate_student,
    ):
        # given
        student = populate_student()

        url = "/api/v1/coordinator/"

        client.force_authenticate(student)

        # when
        response = client.post(url, data={})

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_delete_a_coordinator(
        client, populate_student, populate_coordinator
    ):
        # given
        student = populate_student()
        coordinator = populate_coordinator()

        url = f"/api/v1/coordinator/{coordinator.id}/"

        client.force_authenticate(student)

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_update_a_coordinator(
        client,
        populate_student,
        populate_coordinator,
    ):
        # given
        student = populate_student()
        coordinator = populate_coordinator()

        url = f"/api/v1/coordinator/{coordinator.id}/"

        client.force_authenticate(student)

        # when
        response = client.put(url, data={})

        # assert
        assert response.status_code == 403


@pytest.mark.django_db
class TestLessonPermission:
    @staticmethod
    def test_should_not_be_able_to_list_lessons(
        client,
        populate_student,
    ):
        # given
        student = populate_student()

        url = "/api/v1/lesson/"

        client.force_authenticate(student)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_retrieve_a_lesson(
        client, populate_student, populate_lesson
    ):
        # given
        student = populate_student()
        lesson = populate_lesson()

        url = f"/api/v1/lesson/{lesson.id}/"

        client.force_authenticate(student)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_create_lessons(
        client,
        populate_student,
    ):
        # given
        student = populate_student()

        url = "/api/v1/lesson/"

        client.force_authenticate(student)

        # when
        response = client.post(url, data={})

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_delete_a_lesson(
        client, populate_student, populate_lesson
    ):
        # given
        student = populate_student()
        lesson = populate_lesson()

        url = f"/api/v1/lesson/{lesson.id}/"

        client.force_authenticate(student)

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 403

    @staticmethod
    def test_should_not_be_able_to_update_a_lesson(
        client,
        populate_student,
        populate_lesson,
    ):
        # given
        student = populate_student()
        lesson = populate_lesson()

        url = f"/api/v1/lesson/{lesson.id}/"

        client.force_authenticate(student)

        # when
        response = client.put(url, data={})

        # assert
        assert response.status_code == 403
