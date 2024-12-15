from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Task
from .forms import TaskForm
from .models import CustomUser
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


User = get_user_model()

# Page de base
def base_view(request):
    return render(request, 'base.html')

# Tableau de bord
@login_required
def dashboard(request):
    return render(request, 'index.html')

# Profil utilisateur
@login_required
def profile(request):
    return render(request, 'users-profile.html', {'user': request.user})

# Modifier le profil utilisateur
@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        country = request.POST.get('country')
        phone = request.POST.get('phone')

        # Mise à jour des informations utilisateur
        if full_name:
            first_name, *last_name = full_name.split(maxsplit=1)
            user.first_name = first_name
            user.last_name = " ".join(last_name)
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')

    return render(request, 'edit_profile.html', {'user': user})

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
        # Validation des champs
        if not all([username, email, password, full_name]):
            messages.error(request, "All fields are required!")
            return redirect('register')

        # Vérification des doublons
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('register')

        try:

            # Validation du mot de passe
            try:
                validate_password(password)
            except ValidationError as e:
                messages.error(request, f"Password error: {', '.join(e.messages)}")
                return redirect('register')
            
            # Création de l'utilisateur
            first_name, *last_name = full_name.split(maxsplit=1)
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=" ".join(last_name)
            )
             # Stocker les informations supplémentaires dans le modèle utilisateur personnalisé
            user.country = country
            user.phone = phone
            user.save()

            messages.success(request, "Account created successfully!")
            return render(request, 'pages-register.html')

        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect('register') 
         
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

from django.contrib.auth.models import AbstractUser
from django.db import models


def blank_page(request):
    return render(request, 'pages-blank.html')  # Assurez-vous que ce template existe
def test_create_user(request):
    try:
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
       
        return HttpResponse("User created successfully!")
    except Exception as e:
        return HttpResponse(f"Error: {e}")
