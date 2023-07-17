from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import StudentModel,TeacherModel
from .serializer import (StudentSerializer,TeacherSerializer,TeacherCreateSerializer
                        #  UserRegistrationSerializer
                         )

# class UserRegistrationView(generics.CreateAPIView):
#     serializer_class = UserRegistrationSerializer

class TeacherView(generics.ListAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer

class TeacherCreateView(generics.CreateAPIView):
    serializer_class = TeacherCreateSerializer
    
    def perform_create(self, serializer):
        schools_data = self.request.data.get('schools')  # Assuming you pass school data in the request data
        teacher = serializer.save()
        if schools_data:
            teacher.schools.set(schools_data)


class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer

class StudentView(generics.ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer