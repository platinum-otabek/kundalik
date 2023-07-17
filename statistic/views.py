from django.shortcuts import render
from rest_framework import generics
from .models import GradeModel
from .serializers import GradeSerializer
from config.permissions import TeacherPermission
# Create your views here.

class AddMarkView(generics.CreateAPIView):
    queryset = GradeModel.objects.all()
    serializer_class = GradeSerializer
    permission_classes = (TeacherPermission,)
