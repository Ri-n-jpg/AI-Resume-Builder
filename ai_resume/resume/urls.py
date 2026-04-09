from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),  # 👈 ADD THIS
    path('dashboard/', views.dashboard, name='dashboard'),
path('create/', views.create_resume, name='create_resume'),
    path('edit/<int:id>/', views.edit_resume, name='edit_resume'),
 path('preview/<int:id>/', views.preview_resume, name='preview_resume'),
    ]