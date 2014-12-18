from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    site = models.OneToOneField(Site)

    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)
