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


def apply(request, phone, task):
    import urllib.request
    print('http://sms.tritux.com/v1/send?username=tunihack14&password=json0259&origin=pyShare&destination='+phone+
                           '&text='+request.user.username+'%20['+request.user.email+']%20just%20applied%20to%20your%20task%20'+ str(task).replace(" ","%20"))
    print(urllib.request.urlopen('http://sms.tritux.com/v1/send?username=tunihack14&password=json0259&origin=pyShare&destination='+phone+
                           '&text='+request.user.username+'%20['+request.user.email+']%20just%20applied%20to%20your%20task%20'+ str(task).replace(" ","%20")).read())
    return HttpResponse("Thanks for Applying, an sms was sent to inform the task owner.<br>Good luck!")