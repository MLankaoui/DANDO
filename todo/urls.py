from django.urls import path
from todo.views import home

urlpatterns = [
    path('', home, name='home'),
]