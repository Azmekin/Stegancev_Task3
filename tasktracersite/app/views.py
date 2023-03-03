"""All views:
    TaskTrackerList - made for return all tasks (only for admin)
    TaskTrackerCreate - made for make task (only for authorized)
    TaskTrackerDetail - made for delete or update task (only for authorized)
    WorkplaceTasks - made for return tasks from workplace where id of workplace
is equal request param (only for authorized)
    ProfileAsk - made for return info about profile where id of user equal
request param (only for authorized)
    ShowUserView - made for return info about user where id of user equal
request param (only for authorized)
    CreateUserView - made for make new users (for all)
    BugreportCreate - made for create description about bug (only for authorized)
"""
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from .serializers import *


class TaskTrackerList(generics.ListAPIView):
    """Take list of all tasks"""
    permission_classes = [IsAuthenticated | IsAdminUser]
    serializer_class = TaskTrackerSerializer
    queryset = TaskTracker.objects.all()


class TaskTrackerCreate(generics.CreateAPIView):
    """Create new task"""
    permission_classes = [IsAuthenticated]
    serializer_class = TaskTrackerSerializer


class BugreportCreate(generics.CreateAPIView):
    """Create new bugreport"""
    permission_classes = [IsAuthenticated]
    serializer_class = BugReportSerializer


class TaskTrackerDetail(generics.RetrieveUpdateDestroyAPIView):
    """Delete or update tasks"""
    permission_classes = [IsAuthenticated]
    serializer_class = TaskTrackerSerializer
    queryset = TaskTracker.objects.all()


class ProfileAsk(generics.ListAPIView):
    """Give more info about user"""
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        queryset = Profile.objects.all()
        username = self.request.query_params.get('login', None)
        if username is not None:
            queryset = queryset.filter(login=username)
        else:
            queryset = {}
        return queryset


class WorkplaceTasks(generics.ListAPIView):
    """Give all task from worktable"""
    permission_classes = [IsAuthenticated]
    serializer_class = TaskTrackerSerializer

    def get_queryset(self):
        queryset = TaskTracker.objects.all()
        worplace_id = self.request.query_params.get('worplace_id', None)
        if worplace_id is not None:
            queryset = queryset.filter(workplace_id=worplace_id)
        return queryset


class CreateUserView(generics.CreateAPIView):
    """Create new user"""
    model = get_user_model()
    serializer_class = UserSerializer


class ShowUserView(generics.ListAPIView):
    """Give Info about users"""
    permission_classes = [IsAuthenticated]
    model = get_user_model()
    serializer_class = UserSerializer

    def get_queryset(self):

        queryset = self.model.objects.all()
        username = self.request.query_params.get('login', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        else:
            queryset = {}
        return queryset
