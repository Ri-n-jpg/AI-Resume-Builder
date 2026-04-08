from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Resume
def home(request):
    return render(request, "home.html")
@login_required
def dashboard(request):
    resumes = Resume.objects.filter(user=request.user)
    return render(request, "dashboard.html", {"resumes": resumes})
def create_resume(request):
    if request.method == "POST":
        Resume.objects.create(
            user=request.user,
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            summary=request.POST.get("summary"),
            education=request.POST.get("education"),
            experience=request.POST.get("experience"),
            skills=request.POST.get("skills"),
            template=request.POST.get("template"),
        )

        return redirect("dashboard")

    return render(request, "create_resume.html")
def preview_resume(request, id):
    resume = Resume.objects.get(id=id)

    if resume.template == "template1":
        return render(request, "template1.html", {"resume": resume})

    elif resume.template == "template2":
        return render(request, "template2.html", {"resume": resume})