from django.shortcuts import render

# Create your views here.
def admin_dashboard(request):
  return render(request, "dashboard/admin-dashboard.html")

def user_dashboard(request):
  return render(request, "dashboard/user-dashboard.html")

def test(request):
  return render(request, "test.html")