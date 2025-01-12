from django.urls import path
from tasks.views import admin_dashboard, user_dashboard

urlpatterns = [
    path("admin-dashboard/", admin_dashboard),
    path("user-dashboard/", user_dashboard)
]