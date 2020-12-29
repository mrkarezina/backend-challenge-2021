from rest_framework.decorators import api_view
from django.conf import settings
from django.core.serializers import serialize
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly, IsAuthenticated)
from .models import Upload, UploadPrivate
from app_dir.user.models import Profile


@api_view(['POST'])
def image_upload(request):
    if request.method == 'POST':
        user = request.user
        profile, _ = Profile.objects.get_or_create(user=user)
        image_file = request.FILES['image_file']
        image_type = request.POST['image_type']
        if settings.USE_S3:
            if image_type == 'private':
                upload = UploadPrivate(file=image_file)
                upload.save()
                profile.private_images.add(upload)
            else:
                upload = Upload(file=image_file)
                upload.save()
                profile.public_images.add(upload)
            image_url = upload.file.url
        else:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
        return HttpResponse(f"Image uploaded: {image_url}")


@api_view(['GET'])
def public_image_list(request):
    user = request.user
    profile = Profile.objects.get(id=user.pk)
    queryset = profile.public_images.all()
    urls = [model.file.url for model in queryset]
    return JsonResponse({
        "images": urls
    })
