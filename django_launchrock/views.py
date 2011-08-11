from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from launch.forms import LaunchRockForm
from launch.models import LaunchRock

import datetime

def signup(request):
    if request.method == 'POST':
        form = LaunchRockForm(data=request.POST)
        if form.is_valid():
            launch = LaunchRock(email=form.cleaned_data['email'], sign_date=datetime.datetime.now(), 
                                    ip=request.META['REMOTE_ADDR'], http_refer = request.META['HTTP_REFERER'])
            launch.save()
            return HttpResponseRedirect("/done/")
    else:
        form = LaunchRockForm()
    return render_to_response('launch.html', { 'form': form }, context_instance=RequestContext(request))

def done(request):
    return render_to_response('done.html')