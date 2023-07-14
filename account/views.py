from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import StudentModel,TeacherModel
from .serializer import (StudentSerializer,TeacherSerializer,
                        #  UserRegistrationSerializer
                         )

# class UserRegistrationView(generics.CreateAPIView):
#     serializer_class = UserRegistrationSerializer

class TeacherView(generics.ListCreateAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer

class StudentView(generics.ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer