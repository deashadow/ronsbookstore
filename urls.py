from django.urls import path
from . import views

urlpatterns = [
    path('', views.template, name="template"),
    path('bstore', views.bstore, name="bstore"),
]