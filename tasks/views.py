from django.shortcuts import render
from django.db.models import Count, Q
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task
from django.http import HttpResponse

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