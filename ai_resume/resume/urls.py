from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),  # 👈 ADD THIS

    path('dashboard/', views.dashboard, name='dashboard'),
    ]