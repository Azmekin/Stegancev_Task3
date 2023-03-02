"""tasktracersite URL Configuration

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
from django.urls import path
from .views import *
from django.contrib.auth import get_user_model

urlpatterns = [
    path('get_all/', TaskTrackerList.as_view()),
    path('change_task/<int:pk>', TaskTrackerDetail.as_view()),
    path('create_task/', TaskTrackerCreate.as_view()),
    path('profile/', ProfileAsk.as_view()),
    path('workplace/', WorkplaceTasks.as_view()),
    path('register/', CreateUserView.as_view()),

    path('user/', ShowUserView.as_view()),


]
