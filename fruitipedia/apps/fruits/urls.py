from django.urls import path
from .views import create_fruit, details_fruit, edit_fruit, delete_fruit

urlpatterns = [
    path('create/', create_fruit, name='create-fruit'),
    path('<int:pk>/details/', details_fruit, name='details-fruit'),
    path('<int:pk>/edit/', edit_fruit, name='edit-fruit'),
    path('<int:pk>/delete/', delete_fruit, name='delete-fruit'),
]
