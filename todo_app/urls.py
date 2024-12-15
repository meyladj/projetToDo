from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views



urlpatterns = [
  
     path('', views.base_view, name='base'),  # Dashboard (index.html)
     path('dashboard/', views.dashboard, name='dashboard'),  # Add this line
    path('tasks/', views.task_list, name='task_list'),  # Liste des tâches (tasks.html)
    path('tasks/add/', views.task_add, name='add_task'),
    path('tasks/edit/<int:id>/', views.task_edit, name='task_edit'),  # Modifier une tâche (edit_task.html)
    path('profile/', views.profile, name='user_profile'),  # Profil utilisateur (users-profile.html)
    path('contact/', views.contact, name='contact'),  # Page de contact (pages-contact.html)
    path('login/', auth_views.LoginView.as_view(template_name='pages-login.html'), name='login'), 
    path('register/', views.register_view, name='register'),  # Inscription (pages-register.html)
    path('notes/', views.blank_page, name='notes'),  # Page notes (pages-blank.html)
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('test-create-user/', views.test_create_user, name='test_create_user'),


]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
# todo_app/urls.py

