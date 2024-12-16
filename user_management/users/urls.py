from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello', views.hello_world, name='hello_world'),
    path('users', views.list_users, name='list_users'),
    path('new_user', views.new_user, name='new_user'),
    path('users/<int:id>', views.user_details, name='user_details'),
]
