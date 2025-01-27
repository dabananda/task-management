from django.shortcuts import render
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task
from django.http import HttpResponse

# Create your views here.
def admin_dashboard(request):
  return render(request, "dashboard/admin-dashboard.html")

def user_dashboard(request):
  return render(request, "dashboard/user-dashboard.html")

def test(request):
  return render(request, 'test.html')

def create_task(request):
  employees = Employee.objects.all()
  form = TaskModelForm()
  if request.method == 'POST':
    form = TaskModelForm(request.POST)
    if form.is_valid():
      ''' For Django Model Form Data'''
      form.save()
      return render(request, 'task_form.html', {'form': form, 'message': 'Task ceated successfully!'})

      ''' For Django Form Data '''
      # data = form.cleaned_data
      # title = data.get('title')
      # description = data.get('description')
      # due_date = data.get('due_date')
      # assigned_to = data.get('assigned_to')
      # task = Task.objects.create(title = title, description = description, due_date = due_date)
      # for emp_id in assigned_to:
      #   employee = Employee.objects.get(id = emp_id)
      #   task.assigned_to.add(employee)
      return HttpResponse("Task created successfully!")
  context = {'form': form}
  return render(request, "task_form.html", context)