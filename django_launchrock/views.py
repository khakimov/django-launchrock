from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from launch.forms import LaunchRockForm
from launch.models import LaunchRock
from django.forms import ModelForm
from django import forms

import datetime

class LaunchRockForm(ModelForm):
    class Meta:
        model = LaunchRock
        exclude = ['sign_date', 'ip', 'http_refer']

    def clean_email(self):
        try:
            LaunchRock.objects.get(email=self.cleaned_data['email'])
        except LaunchRock.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError("This is email is already in database.")


def signup(request):
    if request.method == 'POST':
        form = LaunchRockForm(data=request.POST)
        if form.is_valid():
            launch = LaunchRock.objects.create(email=form.cleaned_data['email'], sign_date=datetime.datetime.now(), 
                                    ip=request.META['REMOTE_ADDR'], http_refer = request.META['HTTP_REFERER'])
            return HttpResponseRedirect("/done/")
    else:
        form = LaunchRockForm()
    return render_to_response('launch.html', { 'form': form }, context_instance=RequestContext(request))

def done(request):
    return render_to_response('done.html')