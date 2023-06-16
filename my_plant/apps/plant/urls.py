from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.plant_create, name='plant-create'),
    path('details/<int:pk>/', views.plant_details, name='plant-details'),
    path('edit/<int:pk>/', views.plant_edit, name='plant-edit'),
    path('delete/<int:pk>/', views.plant_delete, name='plant-delete'),
]
