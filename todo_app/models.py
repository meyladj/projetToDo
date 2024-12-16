from django.db import models
from django.utils.timezone import now
from datetime import timedelta
from django.contrib.auth.models import AbstractUser
from django.conf import settings  # Pour AUTH_USER_MODEL




def one_week_hence():
    return now() + timedelta(weeks=1)

class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=255)  # Titre obligatoire
    content = models.TextField(blank=True)  # Contenu facultatif
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    


class Category(models.Model):
    name = models.CharField(max_length=191, unique=True)
    color = models.CharField(max_length=7, default="#cccccc")  # Hex color code for categories

    def __str__(self):
        return self.name

class TaskList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    country = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.username


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    STATUS_CHOICES = [
        ('Finished', 'Finished'),
        ('Processing', 'Processing'),
        ('Cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks',  # Facilite l'accès via user.tasks
        default=1  # À supprimer si le champ doit être obligatoire
    )
    name = models.CharField(max_length=255)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name
    
    

