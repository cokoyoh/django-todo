from django.shortcuts import render, redirect
from .models import TodoList, Category


def index(request):
    todos = TodoList.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        if 'store-todo' in request.POST:
            title = request.POST['description']
            date = str(request.POST['date'])
            category = request.POST['category_select']
            content = title + " -- " + date + " " + category

            Todo = TodoList(title=title, due_date=date, content=content, category=Category.objects.get(name=category))
            Todo.save()

            return redirect('/todo/list')

        if 'delete-todo' in request.POST:
            todo_list_ids = request.POST['checkedbox']

            for todo_id in todo_list_ids:
                todo = TodoList.objects.get(id=int(todo_id))
                todo.delete()

    return render(request, 'index.html', {'todos': todos, 'categories': categories})


