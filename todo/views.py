from django.shortcuts import redirect, render
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