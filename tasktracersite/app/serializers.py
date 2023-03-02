from .models import *
from rest_framework import serializers
from django.contrib.auth import get_user_model  # If used custom user model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ("id", "username", "email", "password",)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class BugReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BugReport
        fields = '__all__'


class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        fields = '__all__'


class TaskTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTracker
        fields = '__all__'
