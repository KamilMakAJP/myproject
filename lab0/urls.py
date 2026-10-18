from django.urls import path
from . import views

urlpatterns = [
    path('', views.lab0_view, name='lab0_home'),
]