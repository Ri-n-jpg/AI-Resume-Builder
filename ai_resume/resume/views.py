# resume/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Resume


def home(request):
    return render(request, "home.html")


@login_required
def dashboard(request):
    resumes = Resume.objects.filter(user=request.user)
    return render(request, "dashboard.html", {"resumes": resumes})


@login_required
def create_resume(request):
    if request.method == "POST":
        Resume.objects.create(
            user=request.user,
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            location=request.POST.get("location"),
            github=request.POST.get("github"),
            linkedin=request.POST.get("linkedin"),
            leetcode=request.POST.get("leetcode"),
            gfg=request.POST.get("gfg"),
            summary=request.POST.get("summary"),
            education=request.POST.get("education"),
            experience=request.POST.get("experience"),
            skills=request.POST.get("skills"),
            template=request.POST.get("template"),
        )
        return redirect("dashboard")

    return render(request, "create_resume.html")


@login_required
def preview_resume(request, id):
    resume = get_object_or_404(Resume, id=id)

    education_list = [e.strip() for e in (resume.education or "").split("\n") if e.strip()]
    experience_list = [e.strip() for e in (resume.experience or "").split("\n") if e.strip()]
    skills_list = [s.strip() for s in (resume.skills or "").split(",") if s.strip()]

    context = {
        "resume": resume,
        "education_list": education_list,
        "experience_list": experience_list,
        "skills_list": skills_list,
    }

    if resume.template == "template2":
        return render(request, "template2.html", context)
    return render(request, "template1.html", context)


# ✅ FIXED: OUTSIDE (separate function)
@login_required
def edit_resume(request, id):
    resume = get_object_or_404(Resume, id=id, user=request.user)

    if request.method == "POST":
        resume.name = request.POST.get("name")
        resume.email = request.POST.get("email")
        resume.phone = request.POST.get("phone")
        resume.location = request.POST.get("location")
        resume.github = request.POST.get("github")
        resume.linkedin = request.POST.get("linkedin")
        resume.leetcode = request.POST.get("leetcode")
        resume.gfg = request.POST.get("gfg")
        resume.summary = request.POST.get("summary")
        resume.education = request.POST.get("education")
        resume.experience = request.POST.get("experience")
        resume.skills = request.POST.get("skills")
        resume.template = request.POST.get("template")

        resume.save()
        return redirect("dashboard")

    return render(request, "edit_resume.html", {"resume": resume})