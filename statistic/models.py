from django.db import models
from account.models import StudentModel,TeacherModel
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class SubjectModel(models.Model):
    name = models.CharField(max_length=15,default='')

    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table = 'subject'

class AttendanceModel(models.Model):
    student = models.ForeignKey(StudentModel,on_delete=models.CASCADE)
    subject= models.ForeignKey(SubjectModel,on_delete=models.SET_NULL)
    teacher = models.ForeignKey(TeacherModel,on_delete=models.SET_NULL)

    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.student.name
    class Meta:
        db_table = 'attendance'

class GradeModel(models.Model):
    student = models.ForeignKey(StudentModel,on_delete=models.CASCADE)
    subject= models.ForeignKey(SubjectModel,on_delete=models.SET_NULL)
    teacher = models.ForeignKey(TeacherModel,on_delete=models.SET_NULL)
    mark = models.PositiveSmallIntegerField(default=0,
                                            validators=[MinValueValidator(0),
                                                        MaxValueValidator(5)
                                            ])
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.student.name
    
    class Meta:
        db_table = 'attendance'