from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    RegisterView,
    LogoutView,
    MeView,
    TaskListCreateView,
    TaskDetailView,
)

urlpatterns = [
    # ── Auth endpoints ──────────────────────────
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/login/',    TokenObtainPairView.as_view(), name='auth-login'),
    path('auth/refresh/',  TokenRefreshView.as_view(), name='auth-refresh'),
    path('auth/logout/',   LogoutView.as_view(), name='auth-logout'),
    path('auth/me/',       MeView.as_view(), name='auth-me'),

    # ── Task endpoints ──────────────────────────
    path('tasks/',         TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]
