from django.contrib import admin
from todo.models import Todos


@admin.register(Todos)
class TodosAdmin(admin.ModelAdmin):
    list_display = ["id", "content"]