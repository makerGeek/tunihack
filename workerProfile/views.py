from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return HttpResponse(request.user.username +' '+str(request.user.groups.all()))
    # return HttpResponseRedirect(
    #     reverse('profiles_profile_detail',
    #             args=[request.user.username]))
