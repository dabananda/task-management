from django.urls import path
from tasks.views import *

urlpatterns = [
  path('admin-dashboard/', admin_dashboard),
  path('user-dashboard/', user_dashboard),
  path('test/', test),
  path('create-task/', create_task)
]