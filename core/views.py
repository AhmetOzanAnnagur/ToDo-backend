from django.http.response import HttpResponse 
from django.shortcuts import render, get_object_or_404, redirect
from core.models import Task, List
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    tasks = []
    
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
        
    context = {
        "tasks": tasks,
        "lists": List.objects.all()
    }
    return render(request, "core/index.html", context)

def showAllTasks(request):
    tasks = []
    
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
        
    context = {
        # "tasks": Task.objects.filter(user=request.user),
        "tasks": tasks,
        "lists": List.objects.all()
    }
    return render(request, "core/tasks.html", context)

def taskDetails(request, slug):
    task = Task.objects.get(slug=slug)
            
    return render(request, "core/taskdetails.html", {"task": task})

def task_by_list(request, slug):
    context = {
        # "movies": Movie.objects.all()
        # "movies": Movie.objects.filter(is_active=True, category__slug=slug),
        # "movies": Movie.objects.filter(is_active=True, categories__slug=slug),
        "tasks": Task.objects.get(slug=slug).task_set.all(),   
        "lists": List.objects.all(),
        "selected_list": slug,
    }
    return render(request, "core/tasks.html", context)

def task_by_is_done(request, is_done):
    req_is_done = True if is_done == 1 else False
    
    tasks = []
    
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user, is_done=req_is_done)
    
    context = {
        # "tasks": Task.objects.filter(user=request.user, is_done=is_done),
        "tasks": tasks,
        "lists": List.objects.all(),
        "selected_list": "1" if req_is_done else "0",
    }
    return render(request, "core/tasks.html", context)
    
def toggle_task_done(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        # Flip the is_done value
        task.is_done = not task.is_done
        task.save()
    
    return redirect(request.META.get("HTTP_REFERER", "home"))

def add_task(request):
    
     
    if request.user.is_authenticated:
        
        if request.method == "POST":
            name = request.POST["taskname"]
            description = request.POST["description"]
            deadline = request.POST["deadline"]
            
            if not name:
                return render(request, "core/addtask.html", {
                    "error": "You must give a name to your task.",
                    "description": description,
                    "deadline": deadline,
                })

            task = Task(
                name=name,
                description=description,
                deadline=deadline,
                user=request.user,
            )
            task.slug = slugify(name)
            task.save()
            return redirect("home")
        
        return render(request, "core/addtask.html")
    
    return redirect("home")
