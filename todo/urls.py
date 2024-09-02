from django.urls import path
from todo.views import home, delete

urlpatterns = [
    path('', home, name='home'),
    path('delete/<int:todo_id>/', delete, name='delete_todo')
]