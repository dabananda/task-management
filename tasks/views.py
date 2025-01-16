from django.http import HttpResponse
from django.shortcuts import render
from tasks.forms import TaskForm
from tasks.models import Employee, Task

# Create your views here.
def admin_dashboard(request):
  return render(request, "dashboard/admin-dashboard.html")

def user_dashboard(request):
  return render(request, "dashboard/user-dashboard.html")

def create_task(request):
  employees = Employee.objects.all()
  form = TaskForm(employees=employees)

  if request.method == "POST":
    form = TaskForm(request.POST, employees=employees)
    if form.is_valid():
      data = form.cleaned_data
      title = data.get("title")
      description = data.get("description")
      due_date = data.get("due_date")
      assigned_to = data.get("assigned_to")
      task = Task.objects.create(title=title, description=description, due_date=due_date)

      for emp_id in assigned_to:
        emp = Employee.objects.get(id=emp_id)
        # task.assign_to.add(emp)
        task.employee.add(emp)
      
      return HttpResponse("Task created successfully")

  context = {
    "form": form
  }
  return render(request, "task_form.html", context)