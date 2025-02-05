from django.shortcuts import render, redirect
from django.db.models import Count, Q
from tasks.forms import TaskForm, TaskModelForm, TaskDetailModelForm
from tasks.models import Employee, Task
from django.http import HttpResponse
from django.contrib import messages

def admin_dashboard(request):
  counts = Task.objects.aggregate(
    total=Count('id'),
    completed=Count('id', filter=Q(status='COMPLETED')),
    in_progress=Count('id', filter=Q(status='IN_PROGRESS')),
    pending=Count('id', filter=Q(status='PENDING')),
  )

  type = request.GET.get('type', 'all')
  base_query = Task.objects.select_related('details').prefetch_related('assigned_to')
  if type == 'completed':
    tasks = base_query.filter(status='COMPLETED')
  elif type == 'in_progress':
    tasks = base_query.filter(status='IN_PROGRESS')
  elif type == 'pending':
    tasks = base_query.filter(status='PENDING')
  else:
    tasks = base_query.all()

  context = {
    "tasks": tasks,
    "counts": counts
  }
  return render(request, "dashboard/admin-dashboard.html", context)

def user_dashboard(request):
  return render(request, "dashboard/user-dashboard.html")

def test(request):
  return render(request, 'test.html')

def create_task(request):
  task_form = TaskModelForm()
  task_detail_form = TaskDetailModelForm()

  if request.method == 'POST':
    task_form = TaskModelForm(request.POST)
    task_detail_form = TaskDetailModelForm(request.POST)

    if task_form.is_valid() and task_detail_form.is_valid():
      ''' For Django Model Form Data'''
      task = task_form.save()
      task_detail = task_detail_form.save(commit=False)
      task_detail.task = task
      task_detail.save()
      messages.success(request, "Task created successfully!")
      return redirect('create-task')
    
  context = {'task_form': task_form, 'task_detail_form': task_detail_form}
  return render(request, "task_form.html", context)

def update_task(request, id):
  task = Task.objects.get(id = id)
  task_form = TaskModelForm(instance = task)

  if task.details:
    task_detail_form = TaskDetailModelForm(instance = task.details)
  
  if request.method == 'POST':
    task_form = TaskModelForm(request.POST, instance = task)
    task_detail_form = TaskDetailModelForm(request.POST, instance = task.details)

    if task_form.is_valid() and task_detail_form.is_valid():
      task_form.save()
      task_detail = task_detail_form.save(commit=False)
      task_detail.task = task
      task_detail.save()

      messages.success(request, "Task updated successfully!")
      return redirect('update-task', id)
    
  context = {'task_form': task_form, 'task_detail_form': task_detail_form}
  return render(request, "task_form.html", context)

def delete_task(request, id):
  if request.method == 'POST':
    task = Task.objects.get(id = id)
    task.delete()
    messages.success(request, "Task deleted successfully")
    return redirect("admin-dashboard")
  else:
    messages.error(request, "Something went wrong")
    return redirect("admin-dashboard")


def view_task(request):
  # retrive all tasks
  tasks = Task.objects.filter(status="PENDING")
  return render(request, "show_task.html", {"tasks": tasks})