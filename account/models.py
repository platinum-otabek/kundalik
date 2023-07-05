from django.db import models
from datetime import datetime
# Create your models here.

class PersonModel(models.Model):
    name = models.CharField(max_length=65,default='')
    fname = models.CharField(max_length=65,default='')
    date_of_birth =models.DateField(default=datetime.now)
    address = models.TextField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        abstract = True

class StudentModel(PersonModel):
    active = models.BooleanField(default=True)
    username = models.CharField(default='',max_length=25)
    password = models.CharField(default='',max_length=65)
    phone = models.CharField(default='',max_length=65)

    class Meta:
        db_table = 'student'
