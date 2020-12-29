from django.db import models
from django.contrib.auth.models import User
from app_dir.images.models import UploadPrivate


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    images = models.ManyToManyField(UploadPrivate)
