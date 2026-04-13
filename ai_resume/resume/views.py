# resume/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from .forms import SignupForm
from .models import Resume, Profile


# ---------------- HOME ----------------
def home(request):
    return render(request, "home.html")


# ---------------- DASHBOARD ----------------
@login_required
def dashboard(request):
    resumes = Resume.objects.filter(user=request.user)
    return render(request, "dashboard.html", {"resumes": resumes})


# ---------------- CREATE RESUME ----------------
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


# ---------------- EDIT RESUME ----------------
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


# ---------------- PREVIEW RESUME ----------------
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


# ---------------- OVERVIEW ----------------
@login_required
def overview(request):
    resumes = Resume.objects.filter(user=request.user)

    context = {
        "total_resumes": resumes.count(),
        "monthly_resumes": resumes.count(),
        "last_resume": resumes.order_by("-id").first(),
    }

    return render(request, "overview.html", context)


# ---------------- TEMPLATE PAGE ----------------
def template(request):
    return render(request, "template.html")


# ---------------- DELETE RESUME ----------------
@login_required
def delete_resume(request, id):
    resume = get_object_or_404(Resume, id=id, user=request.user)

    if request.method == "POST":
        resume.delete()
        return redirect("dashboard")

    return render(request, "confirm_delete.html", {"resume": resume})


# ---------------- SETTINGS ----------------
@login_required
def setting(request):
    return render(request, "setting.html")


# ---------------- UPDATE PROFILE ----------------
@login_required
def update_profile(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get("name")
        user.email = request.POST.get("email")
        user.save()

        messages.success(request, "Profile updated successfully ✅")
        return redirect("settings")

    return redirect("settings")


# ---------------- SIGNUP ----------------
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})


# ---------------- LOGIN ----------------
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password ❌")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


# ---------------- LOGOUT ----------------
def user_logout(request):
    logout(request)
    return redirect("login")


# ---------------- SAVE TEMPLATE ----------------
@login_required
def save_template(request):
    if request.method == "POST":
        template = request.POST.get("template")

        profile, created = Profile.objects.get_or_create(user=request.user)
        profile.default_template = template
        profile.save()

        return redirect("settings")


# ---------------- CHANGE PASSWORD ----------------
@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("settings")
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, "change_password.html", {"form": form})


# ---------------- LOGOUT ALL ----------------
@login_required
def logout_all(request):
    logout(request)
    return redirect("login")


# ---------------- DELETE ACCOUNT ----------------
@login_required
def delete_account(request):
    if request.method == "POST":
        request.user.delete()
        return redirect("home")

    return render(request, "confirm_delete_account.html")