
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('hopitapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
