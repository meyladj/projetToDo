# todo_app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.hashers import make_password

def base_view(request):
    return render(request, 'base.html')  # Associe le template `base.html`

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Email content
        full_message = f"Message from {name} ({email}):\n\n{message}"

        try:
            # Send email
            send_mail(
                subject=subject,
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['meyladjabeee@gmail.com'],  # Replace with your target email address
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, f'Error sending message: {e}')

    return render(request, 'pages-contact.html')
  
def dashboard(request):
    return render(request, 'index.html')  # Dashboard principale

def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # Filtre par utilisateur connecté
    return render(request, 'tasks.html', {'tasks': tasks})  # Liste des tâches


def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
           task = form.save(commit=False)
           task.user = request.user  # Lien avec l'utilisateur connecté
           task.save()
        return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})



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


    if request.method == 'POST':
        user = request.user
        full_name = request.POST.get('fullName')
        # Par exemple, tu peux gérer d'autres champs ici comme le pays
        # country = request.POST.get('Country')

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        country = request.POST.get('country')
        phone = request.POST.get('phone')

        # Mettre à jour les champs
        if hasattr(user, 'profile'):
            user.profile.full_name = full_name
            user.profile.country = country
            user.profile.phone = phone
            user.profile.save()

        return redirect('user_profile')

    return render(request, 'edit_profile.html', {'user': user})
      
def profile(request):
    user = request.user
    return render(request, 'users-profile.html', {'user': user})  # Profil utilisateur

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        country = request.POST.get('country')

    
       # Check for duplicate username or email
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return redirect('register')


        # Create the user and profile
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.profile.full_name = full_name
            user.profile.phone = phone
            user.profile.country = country
            user.profile.save()

            # Authenticate and log the user in
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
            return redirect('register')

    return render(request, 'pages-register.html')
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('login')

    return render(request, 'pages-login.html')


def blank_page(request):
    return render(request, 'pages-blank.html')  # Notes ou pages vierges
def user_profile(request):
    user = request.user
    return render(request, 'users-profile.html', {'user': user})
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        country = request.POST.get('country')
        
        # Mettre à jour les champs
        if full_name:
            first_name, *last_name = full_name.split(maxsplit=1)
            user.first_name = first_name
            user.last_name = ' '.join(last_name)
        
        if hasattr(user, 'profile'):
            user.profile.country = country
            user.profile.save()
        
        user.save()
        return redirect('user_profile')
    
    return render(request, 'edit_profile.html', {'user': user})


