from rest_framework.decorators import api_view
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly, IsAuthenticated)
from .models import Upload, UploadPrivate


@api_view(['POST'])
def image_upload(request):
    if request.method == 'POST':
        image_file = request.FILES['image_file']
        image_type = request.POST['image_type']
        if settings.USE_S3:
            if image_type == 'private':
                upload = UploadPrivate(file=image_file)
            else:
                upload = Upload(file=image_file)
            upload.save()
            image_url = upload.file.url
        else:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
        # TODO: Return link to S3 resource
        return HttpResponse("Image uploaded")
