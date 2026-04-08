from django.db import models
from django.contrib.auth.models import User
class Resume(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=255)
    skills=models.TextField()
    summary=models.TextField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
# Create your models here.
