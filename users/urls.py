from django.urls import path

from users.views import *

app_name = 'users'

urlpatterns = [
    path('', users_list_create_view, name='users_list_create'),
    path('<int:pk>/', user_detail, name='user_detail'),
]
