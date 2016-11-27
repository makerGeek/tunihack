from datetime import timezone, time, datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .forms import TaskForm

# Create your views here.
from postTask.models import Task


@login_required
def postTask(request):
    form = TaskForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            print("valid form !")
            post = form.save()
            post.author = request.user.username
            post.publishdate = datetime.now()
            post.save()
        return HttpResponse("<h2>Task added </h2>")
    else:
        return render(request, 'postTask/post_task.html', {'form': form})
