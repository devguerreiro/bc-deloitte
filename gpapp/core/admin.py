from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from gpapp.core.models.coordinator import Coordinator
from gpapp.core.models.lesson import Lesson
from gpapp.core.models.student import Student
from gpapp.core.models.teacher import Teacher
from gpapp.core.models.user import User

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Coordinator)
admin.site.register(Lesson)
admin.site.register(User, UserAdmin)
