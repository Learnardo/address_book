
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_address', views.add_address, name="add_address"),
    path('edit/<address_id>', views.edit_address, name="edit_address"),
    path('delete/<address_id>', views.delete_address, name="delete_address"),
]
