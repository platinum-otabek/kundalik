from django.urls import path
from .views import AddMarkView

urlpatterns = [
    path('add-create/',AddMarkView.as_view())
]