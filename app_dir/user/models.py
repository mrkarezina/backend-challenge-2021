from django.db import models
from django.contrib.auth.models import User
from app_dir.images.models import Upload, UploadPrivate


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    private_images = models.ManyToManyField(UploadPrivate)
    public_images = models.ManyToManyField(Upload)
