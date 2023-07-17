"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/api/account/',include('account.urls')),
    path('v1/api/statistic/',include('statistic.urls')),
    path('v1/api/statistic/',include('new1.urls')),
    path('v1/api/statistic/',include('new2.urls')),
    path('v1/api/statistic/',include('new3.urls')),
  
]

# create user kundalik_user with encrypted password '#Pg8Lg-$';
# CREATE DATABASE kundalik_db OWNER kundalik_user;
# grant all privileges on database kundalik_db to kundalik_user;

# ALTER ROLE kundalik_user SET client_encoding TO 'utf8';
# ALTER ROLE kundalik_user SET default_transaction_isolation TO 'read committed';
# ALTER ROLE kundalik_user SET timezone TO 'UTC';
