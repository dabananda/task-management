from django.shortcuts import render
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task
from django.http import HttpResponse

def admin_dashboard(request):
  return render(request, "dashboard/admin-dashboard.html")

def user_dashboard(request):
  return render(request, "dashboard/user-dashboard.html")

def test(request):
  return render(request, 'test.html')

def create_task(request):
  form = TaskModelForm()
  if request.method == 'POST':
    form = TaskModelForm(request.POST)
    if form.is_valid():
      ''' For Django Model Form Data'''
      form.save()
      return render(request, 'task_form.html', {'form': form, 'message': 'Task ceated successfully!'})
  context = {'form': form}
  return render(request, "task_form.html", context)

def view_task(request):
  # retrive all tasks
  tasks = Task.objects.filter(status="PENDING")
  return render(request, "show_task.html", {"tasks": tasks})