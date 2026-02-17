from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task


# ──────────────────────────────────────────────
# Auth Serializers
# ──────────────────────────────────────────────

class RegisterSerializer(serializers.ModelSerializer):
    """Handles new user registration."""

    password = serializers.CharField(
        write_only=True,
        min_length=8,
        style={'input_type': 'password'}
    )
    password_confirm = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password_confirm']
        read_only_fields = ['id']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    """Read-only user profile info."""

    class Meta:
        model = User
        fields = ['id', 'username', 'email']


# ──────────────────────────────────────────────
# Task Serializers
# ──────────────────────────────────────────────

class TaskSerializer(serializers.ModelSerializer):
    """Full task serializer — used for create / update."""

    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'owner', 'title', 'description',
            'status', 'priority', 'due_date',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']

    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Title must be at least 3 characters long."
            )
        return value.strip()

    def validate_due_date(self, value):
        from django.utils import timezone
        if value and value < timezone.now().date():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value


class TaskListSerializer(serializers.ModelSerializer):
    """Lightweight serializer — used for list view."""

    class Meta:
        model = Task
        fields = ['id', 'title', 'status', 'priority', 'due_date', 'created_at']
