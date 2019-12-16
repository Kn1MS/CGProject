from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView, name="MainView"),
    path('create_task/', views.CreateTask, name="CreateTask"),
]