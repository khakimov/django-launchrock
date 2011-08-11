from django import forms
from launch.models import LaunchRock

class LaunchRockForm(forms.Form):
    email = forms.EmailField()
    
    def clean_email(self):
        try:
            LaunchRock.objects.get(email=self.cleaned_data['email'])
        except LaunchRock.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError("This is email is already in database.")
