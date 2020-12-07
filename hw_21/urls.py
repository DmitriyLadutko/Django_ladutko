from django.urls import path
from hw_21.views import home_page, add_person

urlpatterns = [
    path('home/', home_page, name='home'),
    path('add_person/', add_person, name='add_person'),

]
