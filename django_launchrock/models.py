from django.db import models

import datetime

class LaunchRock(models.Model):
    email = models.EmailField()
    sign_date = models.DateTimeField(default=datetime.datetime.now)
    ip = models.IPAddressField()
    http_refer = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.email
