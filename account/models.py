from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('a','Admin'),
        ('s','Student'),
        ('t','Teacher'),
        ('p','Parent')
    )
    roles =     models.CharField(max_length=1,choices=ROLE_CHOICES)


class PersonModel(models.Model):
    name = models.CharField(max_length=65,default='')
    fname = models.CharField(max_length=65,default='')
    date_of_birth =models.DateField(default=datetime.now)
    address = models.TextField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None,null=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        abstract = True

class StudentModel(PersonModel):
    active = models.BooleanField(default=True)
    # username = models.CharField(default='',max_length=25)
    # password = models.CharField(default='',max_length=65)
    phone = models.CharField(default='',max_length=65)
    image = models.ImageField(upload_to='upload/student',default='')

    class Meta:
        db_table = 'student'

class TeacherModel(PersonModel):
    from school.models import SchoolModel
    subject = models.ForeignKey('statistic.SubjectModel',on_delete=models.SET_NULL,null=True)
    toifa = models.CharField(max_length=65,default='')
    salary = models.PositiveIntegerField(default=1)
    school = models.ManyToManyField(to=SchoolModel)

    def __str__(self) -> str:
        return self.name

