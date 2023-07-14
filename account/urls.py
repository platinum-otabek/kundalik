
from django.urls import path
from .views import (TeacherView,TeacherDetailView,StudentView,StudentDetailView)

urlpatterns = [
    path('teacher/',TeacherView.as_view()),
    path('teacher/<pk>/',TeacherDetailView.as_view()),
    path('student/',StudentView.as_view()),
    path('student/<pk>/',StudentDetailView.as_view())
]