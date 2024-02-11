"""PennAppsChallenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from pennapps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pennapps.urls')),
    path('application', views.application, name='application'),
    path('application_signup', views.application_signup, name='application_signup'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('signout', views.signout, name='signout'),
    path('createUser', views.login, name='createUser')
]
