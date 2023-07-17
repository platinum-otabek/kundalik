from django.contrib import admin
from .models import SubjectModel,AttendanceModel,GradeModel
# Register your models here.

admin.site.register(SubjectModel)
admin.site.register(AttendanceModel)
admin.site.register(GradeModel)