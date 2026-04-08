from django.db import models
from django.contrib.auth.models import User
class Resume(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=255)
    skills=models.TextField(blank=True)
    education = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    summary=models.TextField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    template = models.CharField(max_length=50, default="template1")
    location = models.CharField(max_length=100, blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    def __str__(self):
        return self.name
# Create your models here.
