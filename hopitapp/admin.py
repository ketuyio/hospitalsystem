from django.contrib import admin
from hopitapp.models import Users
from hopitapp.models import Products,Member,Contacts,ImageModel


# Register your models here.
admin.site.register(Users)
admin.site.register(Products)
admin.site.register(Member)
admin.site.register(Contacts)
admin.site.register(ImageModel)
