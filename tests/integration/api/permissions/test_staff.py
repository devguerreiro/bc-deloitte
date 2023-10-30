import pytest


@pytest.mark.django_db
class TestStudentPermission:
    @staticmethod
    def test_should_be_able_to_get_student_grades(staff_client, populate_student):
        # given
        student = populate_student()

        url = f"/api/v1/student/{student.id}/grades/"

        # when
        response = staff_client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_be_able_to_list_students(staff_client):
        # given
        url = "/api/v1/student/"

        # when
        response = staff_client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_be_able_to_retrieve_student(staff_client, populate_student):
        # given
        student = populate_student()

        url = f"/api/v1/student/{student.id}/"

        # when
        response = staff_client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_be_able_to_create_students(staff_client):
        # given
        url = "/api/v1/student/"

        # when
        response = staff_client.post(url, data={})

        # assert
        assert response.status_code == 400

    @staticmethod
    def test_should_be_able_to_delete_student(staff_client, populate_student):
        # given
        student = populate_student()

        url = f"/api/v1/student/{student.id}/"

        # when
        response = staff_client.delete(url)

        # assert
        assert response.status_code == 204

    @staticmethod
    def test_should_be_able_to_update_student(staff_client, populate_student):
        # given
        student = populate_student()

        url = f"/api/v1/student/{student.id}/"

        # when
        response = staff_client.put(url, data={})

        # assert
        assert response.status_code == 400


@pytest.mark.django_db
class TestTeacherPermission:
    @staticmethod
    def test_should_be_able_to_list_teachers(staff_client):
        # given
        url = "/api/v1/teacher/"

        # when
        response = staff_client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_be_able_to_retrieve_a_teacher(staff_client, populate_teacher):
        # given
        teacher = populate_teacher()

        url = f"/api/v1/teacher/{teacher.id}/"

        # when
        response = staff_client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_be_able_to_create_teachers(staff_client):
        # given
        url = "/api/v1/teacher/"

        # when
        response = staff_client.post(url, data={})

        # assert
        assert response.status_code == 400

    @staticmethod
    def test_should_be_able_to_delete_a_teacher(staff_client, populate_teacher):
        # given
        teacher = populate_teacher()

        url = f"/api/v1/teacher/{teacher.id}/"

        # when
        response = staff_client.delete(url)

        # assert
        assert response.status_code == 204

    @staticmethod
    def test_should_be_able_to_update_a_teacher(staff_client, populate_teacher):
        # given
        teacher = populate_teacher()

        url = f"/api/v1/teacher/{teacher.id}/"

        # when
        response = staff_client.put(url, data={})

        # assert
        assert response.status_code == 400


@pytest.mark.django_db
class TestCoordinatorPermission:
    @staticmethod
    def test_should_be_able_to_list_coordinators(staff_client):
        # given
        url = "/api/v1/coordinator/"

        # when
        response = staff_client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_be_able_to_retrieve_a_coordinator(
        staff_client, populate_coordinator
    ):
        # given
        coordinator = populate_coordinator()

        url = f"/api/v1/coordinator/{coordinator.id}/"

        # when
        response = staff_client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_be_able_to_create_coordinators(staff_client):
        # given
        url = "/api/v1/coordinator/"

        # when
        response = staff_client.post(url, data={})

        # assert
        assert response.status_code == 400

    @staticmethod
    def test_should_be_able_to_delete_a_coordinator(staff_client, populate_coordinator):
        # given
        coordinator = populate_coordinator()

        url = f"/api/v1/coordinator/{coordinator.id}/"

        # when
        response = staff_client.delete(url)

        # assert
        assert response.status_code == 204

    @staticmethod
    def test_should_be_able_to_update_a_coordinator(staff_client, populate_coordinator):
        # given
        coordinator = populate_coordinator()

        url = f"/api/v1/coordinator/{coordinator.id}/"

        # when
        response = staff_client.put(url, data={})

        # assert
        assert response.status_code == 400


@pytest.mark.django_db
class TestLessonPermission:
    @staticmethod
    def test_should_be_able_to_list_lessons(staff_client):
        # given
        url = "/api/v1/lesson/"

        # when
        response = staff_client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_be_able_to_retrieve_a_lesson(staff_client, populate_lesson):
        # given
        lesson = populate_lesson()

        url = f"/api/v1/lesson/{lesson.id}/"

        # when
        response = staff_client.get(url)

        # assert
        assert response.status_code == 200

    @staticmethod
    def test_should_be_able_to_create_lessons(staff_client):
        # given
        url = "/api/v1/lesson/"

        # when
        response = staff_client.post(url, data={})

        # assert
        assert response.status_code == 400

    @staticmethod
    def test_should_be_able_to_delete_a_lesson(staff_client, populate_lesson):
        # given
        lesson = populate_lesson()

        url = f"/api/v1/lesson/{lesson.id}/"

        # when
        response = staff_client.delete(url)

        # assert
        assert response.status_code == 204

    @staticmethod
    def test_should_be_able_to_update_a_lesson(staff_client, populate_lesson):
        # given
        lesson = populate_lesson()

        url = f"/api/v1/lesson/{lesson.id}/"

        # when
        response = staff_client.put(url, data={})

        # assert
        assert response.status_code == 400

    @staticmethod
    def test_should_be_able_to_update_the_student_grades(
        staff_client, populate_lesson_grade
    ):
        # given
        lesson_grade = populate_lesson_grade()

        url = f"/api/v1/lesson/{lesson_grade.lesson.id}/student_grades/"

        # when
        response = staff_client.put(url, data={})

        # assert
        assert response.status_code == 404
