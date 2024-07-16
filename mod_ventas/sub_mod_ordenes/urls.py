from django.urls import path
from . import views


urlpatterns = [
    path('', views.ordenes, name="ordenes")
]
