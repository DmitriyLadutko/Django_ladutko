from django.urls import path
from Cw20.views import *

urlpatterns = [
    path('write_file/', write_file, name='write_file'),
    path('read_file/', read_file, name='read_file'),
    path('clear_file/', clear_file, name='clear_file'),
]
