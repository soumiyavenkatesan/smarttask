from django.shortcuts import render, redirect
from .models import Task

def home(request):
    filter_type = request.GET.get('filter')

    if filter_type == 'completed':
        tasks = Task.objects.filter(completed=True)
    elif filter_type == 'pending':
        tasks = Task.objects.filter(completed=False)
    else:
        tasks = Task.objects.all()

    total = Task.objects.count()
    completed = Task.objects.filter(completed=True).count()
    pending = Task.objects.filter(completed=False).count()

    return render(request, 'home.html', {
        'tasks': tasks,
        'total': total,
        'completed': completed,
        'pending': pending
    })
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        priority = request.POST.get('priority')
        Task.objects.create(title=title, priority=priority)
        return redirect('/')
    return render(request, 'add.html')

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/')
def update_task(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.save()
        return redirect('/')

    return render(request, 'update.html', {'task': task})
def toggle_complete(request, id):
    task = Task.objects.get(id=id)
    task.completed = not task.completed
    task.save()
    return redirect('/')