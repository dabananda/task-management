from django.urls import path
from tasks.views import admin_dashboard, user_dashboard, create_task

urlpatterns = [
    path("admin-dashboard/", admin_dashboard),
    path("user-dashboard/", user_dashboard),
    path("create-task/", create_task)
]