# resume/models.py
from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Personal information
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)

    # Resume sections
    summary = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    skills = models.TextField(blank=True)

    # Template
    template = models.CharField(max_length=50, default="template1")

    # Profile links
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    leetcode = models.URLField(blank=True)
    gfg = models.URLField(blank=True)

    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_template = models.CharField(max_length=20, default="template1")

    def __str__(self):
        return self.user.username