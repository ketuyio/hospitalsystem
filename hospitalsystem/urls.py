
from django.contrib import admin
from django.urls import path
from hopitapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.index,name='index'),
    path('inner-page/', views.inner,name='inner-page'),
    path('register/', views.register,name='register'),
    path('login/', views.login,name='login'),
]
