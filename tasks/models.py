from django.db import models

class Employee(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)

class Project(models.Model):
  name = models.CharField(max_length=100)
  start_date = models.DateField()

class Task(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
  employee = models.ManyToManyField(Employee)
  title = models.CharField(max_length=100)
  description = models.TextField()
  is_completed = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class TaskDetails(models.Model):
  LOW = 'L'
  MEDIUM = 'M'
  HIGH = 'H'
  PRIORITY_OPTIONS = (
    (LOW, 'Low'),
    (MEDIUM, 'Medium'),
    (HIGH, 'High'),
  )
  task = models.OneToOneField(Task, on_delete=models.CASCADE)
  assigned_to = models.CharField(max_length=100)
  priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default=LOW)