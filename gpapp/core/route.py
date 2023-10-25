from rest_framework.routers import DefaultRouter

from gpapp.core.views.student import StudentViewSet

router = DefaultRouter()

router.register("student", StudentViewSet, basename="student")
