from django.contrib.auth.models import AbstractUser
from django.db import models

class Package(models.Model):
    name = models.CharField(max_length=50)
    can_upload = models.BooleanField(default=True)
    can_preview = models.BooleanField(default=True)
    can_delete = models.BooleanField(default=True)
    can_download = models.BooleanField(default=True)
    can_share = models.BooleanField(default=True)

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    package = models.ForeignKey(Package, null=True, blank=True, on_delete=models.SET_NULL)
