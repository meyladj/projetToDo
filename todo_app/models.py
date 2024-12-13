from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import timedelta
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import IntegrityError




def one_week_hence():
    return now() + timedelta(weeks=1)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name
    

#class UserProfile(models.Model):
   # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  #  about = models.TextField(blank=True, null=True)
   # country = models.CharField(max_length=100, blank=True, null=True)
   # address = models.TextField(blank=True, null=True)
   # phone = models.CharField(max_length=15, blank=True, null=True)

class TaskList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # Name of the task list
    description = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return self.name


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Add this line
    name = models.CharField(max_length=255)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    category = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    due_date = models.DateTimeField(default=one_week_hence)  # Add this if not already defined

    def __str__(self):
        return self.name
    
    

