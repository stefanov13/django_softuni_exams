from django.urls import path, include

from . import views

urlpatterns = [
    path('create/', views.create_profile, name='create-profile'),
    path('details/', views.profile_details, name='profile-details'),
    path('edit/', views.profile_edit, name='profile-edit'),
    path('delete/', views.profile_delete, name='profile-delete'),

]
