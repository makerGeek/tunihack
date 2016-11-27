import json
from datetime import timezone, time, datetime
from json.decoder import JSONArray

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import QuerySet
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

@login_required
def findTask(request):
    html =''
    if (request.user.username != ""):
        html+='<a href="/accounts/logout">logout</a>'
    html += '<ol>'
    all_tasks = Task.objects.all()
    for task in all_tasks:
        spaces_free_title = task.title.replace(" ","%20");
        html+='<br><br><li><ul> title : '+task.title+'</ul><ul> description: '+task.description+'</ul><ul>author :' +task.author+'</ul>' \
             '<ul><a href="/apply/'+ task.phone+'/'+spaces_free_title+'">Apply</a></ul></li>'
    html+='</ol>'
    return HttpResponse(html)


def jobs_by_city(request, city):
    class Public_task(object):
        title=''
        description =''
        region=''
        skills=''

        def __init__(self, title, description, region, skills):
            self.title =title
            self.description = description
            self.region = region
            self.skills = skills

    relevant_tasks = Task.objects.filter(city__contains=city)
    new_task_set = [];
    import jsonpickle
    for task in relevant_tasks:
        new_task = Public_task(title=task.title, description=task.description, region=task.region,skills=task.skills)
        new_task_set.append(new_task)
    # leads_as_json = serializers.serialize('json', relevant_tasks)
    # return HttpResponse(leads_as_json, content_type='json')
    print(json.dumps(json.loads(jsonpickle.encode(new_task_set, unpicklable=False)), indent=2))

    return HttpResponse(json.dumps(json.loads(jsonpickle.encode(new_task_set, unpicklable=False)), indent=2))