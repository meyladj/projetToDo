from django.db import models
from django.utils.timezone import now
from datetime import timedelta
from django.contrib.auth.models import AbstractUser
from django.conf import settings  # Pour AUTH_USER_MODEL




def one_week_hence():
    return now() + timedelta(weeks=1)



#class UserProfile(models.Model):
   # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  #  about = models.TextField(blank=True, null=True)
   # country = models.CharField(max_length=100, blank=True, null=True)
   # address = models.TextField(blank=True, null=True)
   # phone = models.CharField(max_length=15, blank=True, null=True)
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
    category = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    due_date = models.DateTimeField(default=one_week_hence)  # Add this if not already defined

    def __str__(self):
        return self.name
    
    

