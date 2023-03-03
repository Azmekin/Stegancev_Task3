"""tasktracersite URL Configuration

What we have:
get_all/ - take all tasks from table (only for authorized admin)
change_task/<int:pk> - update or delete task
create_task/ - create task
profile/?login=<int> - get addicted info about user with equal id
user/?login=<int> - get main info about user with equal id
workspace/?workplace_id=<int>  - get all tasks in the workspace with equal id
register/ - create new user
bugreport/ - send bugreport
"""
from django.urls import path
from .views import *


urlpatterns = [
    path('get_all/', TaskTrackerList.as_view()),
    path('change_task/<int:pk>', TaskTrackerDetail.as_view()),
    path('create_task/', TaskTrackerCreate.as_view()),
    path('profile/', ProfileAsk.as_view()),
    path('workplace/', WorkplaceTasks.as_view()),
    path('register/', CreateUserView.as_view()),
    path('user/', ShowUserView.as_view()),
    path('bugreport/', BugreportCreate.as_view()),


]
