from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.task, name='task'),
    path('remove/<int:pk>/', views.removal, name='removal'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('completed/', views.completed, name='completed'),
]