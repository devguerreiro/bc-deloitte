from rest_framework.routers import DefaultRouter

from gpapp.core.views.coordinator import CoordinatorViewSet
from gpapp.core.views.student import StudentViewSet
from gpapp.core.views.teacher import TeacherViewSet

router = DefaultRouter()

router.register("student", StudentViewSet, basename="student")
router.register("teacher", TeacherViewSet, basename="teacher")
router.register("coordinator", CoordinatorViewSet, basename="coordinator")
