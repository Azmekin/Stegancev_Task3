from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import *
from rest_framework import generics


class TaskTrackerList(generics.ListAPIView):
    """Take list of all tasks"""
    permission_classes = [IsAuthenticated | IsAdminUser]
    serializer_class = TaskTrackerSerializer
    queryset = TaskTracker.objects.all()


class TaskTrackerCreate(generics.CreateAPIView):
    """Create new task"""
    permission_classes = [IsAuthenticated]
    serializer_class = TaskTrackerSerializer


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


class CreateUserView(CreateAPIView):
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

