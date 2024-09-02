from django.urls import path
from todo.views import home, delete_todo, update_todo

urlpatterns = [
    path('', home, name='home'),
    path('delete/<int:todo_id>/', delete_todo, name='delete_todo'),
    path('update/<int:todo_id>/', update_todo, name='update_todo')
]