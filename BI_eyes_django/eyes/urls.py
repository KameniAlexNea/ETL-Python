from django.urls import include, path
from django.contrib import admin

from .views import upload_file

app_name = 'eyes'
urlpatterns = [
    path('', upload_file, name="upload")
]
