from django.urls import path
from tasks.views import show_tasks, show_specific_task

urlpatterns = [
    path('show-tasks/', show_tasks),
    path('show_specific_task/', show_specific_task)
]