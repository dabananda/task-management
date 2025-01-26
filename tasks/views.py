from django.shortcuts import render
from tasks.forms import TaskForm
from tasks.models import Employee

# Create your views here.
def admin_dashboard(request):
  return render(request, "dashboard/admin-dashboard.html")

def user_dashboard(request):
  return render(request, "dashboard/user-dashboard.html")

def test(request):
  return render(request, 'test.html')

def create_task(request):
  employees = Employee.objects.all()
  form = TaskForm(employees = employees)
  context = {'form': form}
  return render(request, "task_form.html", context)