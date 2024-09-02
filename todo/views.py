from django.shortcuts import redirect, render
from todo.models import Todos


def home(request):
    if request.method == "POST":
        content = request.POST.get('content')
        if content != None:
            Todos.objects.create(content=content)
            return redirect('home')

    todos = Todos.objects.all()
    return render(request, 'index.html', {'todos': todos})