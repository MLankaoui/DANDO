from django.shortcuts import redirect, render, get_object_or_404
from todo.models import Todos


def home(request):
    context = {}

    if request.method == 'POST':
        content = request.POST.get('content') # retrieving data from the post request

        if content != None:
            Todos.objects.create(content=content)
            return redirect('home')
        
    context = {
        "todos": Todos.objects.all()
    }    
    return render(request, 'index.html', context)


def delete(request, todo_id):

    if request.method == 'POST':
        todo = get_object_or_404(Todos, id=todo_id)
        todo.delete()
        return redirect('home')
    