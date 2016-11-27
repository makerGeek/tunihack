from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect

from  workerProfile import views


def index(request):
    if (request.user.username == ""):
        return HttpResponse(
            '<h1>Hi There!<br> Please <a href="/accounts/login">Login</a> or <a href="/accounts/register">Sign up</a></h1>')

    else:
        return redirect('/welcome')

@login_required
def welcome(request):
    return HttpResponse(
        '<h3>Welcome ' + str(request.user.username)+ ', do you want to <a href="/postTask">post a task</a> or  <a href="/findTask">find a task</a> </h3>')
