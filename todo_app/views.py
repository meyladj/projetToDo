import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Note, Task, Category
import json
from .forms import TaskForm
from .models import CustomUser
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from django.utils.timezone import now
from django.db.models import Count, Q
from django.db.models.functions import TruncDay, TruncWeek, TruncMonth
from django.db.models.functions import ExtractWeekDay

User = get_user_model()
def base_view(request):
    return render(request, 'base.html') 
@login_required
def dashboard(request):
    today = now().date()

    # --- LOGIC FOR TOP CARDS ---
    start_of_week = today - timedelta(days=today.weekday())  # Start of the week
    start_of_month = today.replace(day=1)  # Start of the month

    # Count tasks for the cards
    tasks_today = Task.objects.filter(end_time__date=today).count()
    tasks_this_week = Task.objects.filter(end_time__date__gte=start_of_week).count()
    tasks_this_month = Task.objects.filter(end_time__date__gte=start_of_month).count()

    status_counts = {
        'completed': Task.objects.filter(status='Finished').count(),
        'in_progress': Task.objects.filter(status='Processing').count(),
        'canceled': Task.objects.filter(status='Cancelled').count(),
    }


    # --- LOGIC FOR THE DONUT CHART ---
    # Get the filter for the donut chart
    filter_type = request.GET.get('filter', 'month')

    # Determine start date for the donut chart filter
    if filter_type == 'day':
        start_date = today
    elif filter_type == 'week':
        start_date = start_of_week
    else:  # Default: month
        start_date = start_of_month

    # Filter tasks by the selected date range for the donut chart
    tasks_for_chart = Task.objects.filter(end_time__date__gte=start_date)
    total_tasks_for_chart = tasks_for_chart.count()

    # Count tasks grouped by category
    categories = Category.objects.annotate(
        task_count=Count('tasks', filter=Q(tasks__in=tasks_for_chart))
    )

    # Prepare data for the donut chart
    category_data = [
        {
            "name": category.name,
            "value": category.task_count or 0,  # Changed from count to value for consistency
            "color": category.color or "#d3d3d3",  # Default grey color
        }
        for category in categories
    ]

    # Fallback for no categories or no tasks
    if total_tasks_for_chart == 0 or not category_data:
        category_data = [{"name": "No Category", "value": 0, "color": "#d3d3d3"}]
    print("Category Data:", category_data)
    print(json.dumps(category_data, indent=4))
    # --- LOGIC FOR THE WEEKLY GRAPH ---
    # Task counts grouped by weekday
    weekly_data = Task.objects.filter(end_time__date__gte=start_of_week).annotate(
        weekday=ExtractWeekDay('end_time')  # Returns 1 (Sunday) through 7 (Saturday)
    ).values('weekday', 'status').annotate(
        count=Count('id')
    ).order_by('weekday')

    # Prepare the data for the graph
    weekday_mapping = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    graph_data = {status: [0] * 7 for status in ['Finished', 'Processing', 'Cancelled']}

    for entry in weekly_data:
        day_index = (entry['weekday'] - 1) % 7  # Adjust Sunday to be last
        graph_data[entry['status']][day_index] = entry['count']

    # Convert to JSON for the template
    graph_data_json = json.dumps({
        'days': [weekday_mapping[i] for i in range(1, 8)],
        'finished': graph_data['Finished'],
        'processing': graph_data['Processing'],
        'cancelled': graph_data['Cancelled'],
    })

    # Pass data to the template
    return render(request, 'index.html', {
        'tasks_today': tasks_today,
        'tasks_this_week': tasks_this_week,
        'tasks_this_month': tasks_this_month,
        'category_data_json': json.dumps(category_data),  # Pass JSON data for the donut chart
        'filter_type': filter_type,
        'status_counts_json': json.dumps(status_counts),
        'graph_data_json': graph_data_json,  # Pass JSON data for the graph
    })

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
            task.user = request.user  # Associe la tâche à l'utilisateur connecté
            task.save()
            messages.success(request, 'Task added successfully!')
            return redirect('task_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TaskForm()

    # Rendu du formulaire avec les erreurs ou formulaire vide
    return render(request, 'tasks.html', {'form': form})

@login_required
def add_note(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        note = Note.objects.create(
            user=request.user,
            title=data.get("title", "Nouveau titre"),
            content=data.get("content", "")
        )
        return JsonResponse({"id": note.id, "title": note.title, "content": note.content})
    return JsonResponse({"error": "Invalid request"}, status=400)
    
@login_required
def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('color')
        if name and color:
            category = Category.objects.create(name=name, color=color)
            return JsonResponse({'id': category.id, 'name': category.name, 'color': category.color})
    return JsonResponse({'error': 'Invalid data'}, status=400)
# Éditer une tâche
@login_required
def edit_task(request, task_id):
    if request.method == 'POST':
        import json
        task = get_object_or_404(Task, id=task_id, user=request.user)
        data = json.loads(request.body)
        task.name = data.get('name', task.name)
        task.priority = data.get('priority', task.priority)
        task.category.name = data.get('category', task.category.name)
        task.start_time = data.get('start_time', task.start_time)
        task.end_time = data.get('end_time', task.end_time)
        task.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

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

@login_required
def notes_view(request):
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'pages-blank.html', {'notes': notes})

@login_required
def edit_note(request, note_id):
    if request.method == "POST":
        import json
        note = get_object_or_404(Note, id=note_id, user=request.user)
        data = json.loads(request.body)
        if "title" in data:
            note.title = data["title"]
        if "content" in data:
            note.content = data["content"]
        note.save()
        return JsonResponse({"status": "success"})
    return JsonResponse({"error": "Invalid request"}, status=400)

@login_required
def delete_note(request, note_id):
    if request.method == "POST":
        note = get_object_or_404(Note, id=note_id, user=request.user)
        note.delete()
        return JsonResponse({"status": "success"})
    return
@login_required
def task_details(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    return JsonResponse({
        'name': task.name,
        'priority': task.priority,
        'category': task.category.name,  # Utilise le champ de catégorie
        'start_time': task.start_time.isoformat(),
        'end_time': task.end_time.isoformat(),
    })

@login_required
def delete_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id, user=request.user)
        task.delete()
        return JsonResponse({"status": "success"})
    return JsonResponse({"error": "Invalid request"}, status=400)



def blank_page(request):
    return render(request, 'pages-blank.html')  # Assurez-vous que ce template existe
def test_create_user(request):
    try:
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
       
        return HttpResponse("User created successfully!")
    except Exception as e:
        return HttpResponse(f"Error: {e}")
