from django.urls import path
from . import views
urlpatterns = [
 path('', views.home, name='home'),
  # SETTINGS
path('dashboard/', views.dashboard, name='dashboard'),
path('create/', views.create_resume, name='create_resume'),

path('edit/<int:id>/', views.edit_resume, name='edit_resume'),
path('preview/<int:id>/', views.preview_resume, name='preview_resume'),

path('overview/', views.overview, name='overview'),
path('template/', views.template, name='template'),

# SETTINGS
path('settings/', views.setting, name='settings'),
path('settings/update-profile/', views.update_profile, name='update_profile'),

# AUTH
path('login/', views.user_login, name='login'),
path('logout/', views.user_logout, name='logout'),
path('signup/', views.signup, name='signup'),

# FEATURES
path('save-template/', views.save_template, name='save_template'),
path('change-password/', views.change_password, name='change_password'),
path('logout-all/', views.logout_all, name='logout_all'),
path('delete-account/', views.delete_account, name='delete_account'),

# DELETE
path('delete/<int:id>/', views.delete_resume, name='delete_resume'),

# DOWNLOAD (ONLY ONE)
path('download/<int:id>/<str:template>/', views.download_pdf, name='download_pdf'),
   ]