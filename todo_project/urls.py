# todo_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Interface d'administration Django
    path('', include('todo_app.urls')),  # Inclut les URLs de l'application todo_app
]
