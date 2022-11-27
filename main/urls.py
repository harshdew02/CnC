from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index , name="blogHome"),
    path('club-name', views.blogpost ,name="blogpost" ),
    path('contact', views.contact , name="contact")
]