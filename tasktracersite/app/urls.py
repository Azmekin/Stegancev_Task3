"""tasktracersite URL Configuration

What we have:
get_all/ - take all tasks from table (only for authorized admin)
change_task/<int:pk> - update or delete task (only for authorized)
create_task/ - create task (only for authorized)
profile/?login=<int> - get addicted info about user with equal id (only for authorized)
user/?login=<int> - get main info about user with equal id (only for authorized)
workspace/?workplace_id=<int>  - get all tasks in the workspace with equal id (only for authorized)
register/ - create new user (for all)
bugreport/ - send bugreport (only for authorized)
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
