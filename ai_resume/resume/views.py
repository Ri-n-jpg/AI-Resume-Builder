from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Resume
def home(request):
    return render(request, "home.html")
@login_required
def dashboard(request):
    resumes = Resume.objects.filter(user=request.user)
    return render(request, "dashboard.html", {"resumes": resumes})

