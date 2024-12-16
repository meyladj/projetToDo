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
    path('tasks/details/<int:task_id>/', views.task_details, name='task_details'),
path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'),

    path('profile/', views.profile, name='user_profile'),  # Profil utilisateur (users-profile.html)
    path('contact/', views.contact, name='contact'),  # Page de contact (pages-contact.html)
    path('login/', auth_views.LoginView.as_view(template_name='pages-login.html'), name='login'), 
    path('register/', views.register_view, name='register'),  # Inscription (pages-register.html)
    path('notes/', views.blank_page, name='notes'),  # Page notes (pages-blank.html)
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('test-create-user/', views.test_create_user, name='test_create_user'),
    path('tasks/add-category/', views.add_category, name='add_category'),
    path('notes/edit/<int:note_id>/', views.edit_note, name='edit_note'),
    path('notes/add/', views.add_note, name='add_note'),
path('notes/edit/<int:note_id>/', views.edit_note, name='edit_note'),
path('notes/delete/<int:note_id>/', views.delete_note, name='delete_note'),
path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
path('categories/add/', views.add_category, name='add_category'),
path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),




]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
# todo_app/urls.py

