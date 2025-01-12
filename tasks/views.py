from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse("Welcome to the Tasks Home")

def contact(request):
  return HttpResponse("Welcome to the Tasks Contact")

def show_tasks(request):
  return HttpResponse("Show tasks")

def show_specific_task(request, id):
  return HttpResponse(f'This is task of id {id}')