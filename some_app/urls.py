from django.urls import path
from some_app.views import hello_user

urlpatterns = [
    path('hello_user/', hello_user, name='hello_user'),
]
