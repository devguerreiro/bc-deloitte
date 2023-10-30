from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from gpapp.core.models.lesson import Lesson, LessonGrade
from gpapp.core.models.user import User


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("profile",)}),)
    list_display = ["name", "email", "username", "dob", "profile"]
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": ("name", "email", "dob", "profile"),
            },
        ),
    )


admin.site.register(Lesson)
admin.site.register(LessonGrade)
admin.site.register(User, CustomUserAdmin)
