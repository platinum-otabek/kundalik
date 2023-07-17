from django.contrib import admin
from .models import StudentModel,TeacherModel,CustomUser
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username", "first_name",'roles')
    list_filter = ("username", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions",'roles'
            )
            }
        ),
       
    )
    search_fields = ("username",)
    ordering = ("username",)


admin.site.register(CustomUser,CustomUserAdmin)

admin.site.register(TeacherModel)
admin.site.register(StudentModel)