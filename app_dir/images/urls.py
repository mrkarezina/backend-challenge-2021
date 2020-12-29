from django.urls import path

from .views import (
    image_upload,
    public_image_list
)


urlpatterns = [
    path('upload', image_upload, name='image_upload'),
    path('public', public_image_list, name='image_list')
]
