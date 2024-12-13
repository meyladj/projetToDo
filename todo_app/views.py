from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from .models import Task, Profile
from .forms import TaskForm
import logging
from django.db import IntegrityError

logger = logging.getLogger(__name__)

# Page de base
def base_view(request):
    return render(request, 'base.html')


# Création automatique du profil utilisateur
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Vue de contact
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"Message from {name} ({email}):\n\n{message}"

        try:
            send_mail(
                subject=subject,
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['meyladjabeee@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, f'Error sending message: {e}')

    return render(request, 'pages-contact.html')


# Tableau de bord
@login_required
def dashboard(request):
    return render(request, 'index.html')


# Liste des tâches
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks.html', {'tasks': tasks})


# Ajouter une tâche
@login_required
def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})


# Éditer une tâche
@login_required
def task_edit(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})


# Profil utilisateur
@login_required
def profile(request):
    user = request.user
    return render(request, 'users-profile.html', {'user': user})


# Éditer le profil
@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        country = request.POST.get('country')
        phone = request.POST.get('phone')

        if hasattr(user, 'profile'):
            user.profile.full_name = full_name
            user.profile.country = country
            user.profile.phone = phone
            user.profile.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')

    return render(request, 'edit_profile.html', {'user': user})


# Inscription
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        country = request.POST.get('country')

        print(f"Register data: username={username}, email={email}, full_name={full_name}")

        # Vérification des champs obligatoires
        if not all([username, email, password, full_name, phone, country]):
            messages.error(request, "All fields are required!")
            print("Fields missing")
            return redirect('register')

        # Vérification des doublons
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            print("Username exists")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            print("Email exists")
            return redirect('register')

        try:
            # Création de l'utilisateur
            user = User.objects.create_user(username=username, email=email, password=password)
            # Création du profil utilisateur
            Profile.objects.create(user=user, full_name=full_name, phone=phone, country=country)
            
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')

        except IntegrityError as e:
            messages.error(request, f"Database error: {e}")
            print(f"Database error: {e}")
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")
            print(f"Unexpected error: {e}")


    return render(request, 'pages-register.html')

# Connexion
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password!')

    return render(request, 'pages-login.html')

def blank_page(request):
    return render(request, 'pages-blank.html')  # Assurez-vous que ce template existe
def test_create_user(request):
    try:
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
        Profile.objects.create(user=user, full_name='Test User', phone='123456789', country='TestLand')
        return HttpResponse("User created successfully!")
    except Exception as e:
        return HttpResponse(f"Error: {e}")
