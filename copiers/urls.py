from django.urls import path
from .views import home, add_copier, edit_copier, delete_copier, confirm_delete_copier


urlpatterns = [
    path('', home, name='home'),
    path('add/', add_copier, name='add_copier'),
    path('edit/<int:pk>/', edit_copier, name='edit_copier'),
    path('delete/<int:id>/', delete_copier, name='delete_copier'),
    path('delete/<int:id>/confirm/', confirm_delete_copier, name='confirm_delete_copier'),
]
