from django.contrib import admin
from .models import StudentModel,TeacherModel,CustomUser
# Register your models here.


admin.site.register(TeacherModel)
admin.site.register(StudentModel)
admin.site.register(CustomUser)