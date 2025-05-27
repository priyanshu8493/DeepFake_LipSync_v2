from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_script, name='upload_script'),
]
