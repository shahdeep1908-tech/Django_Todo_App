from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TodoForm
from .models import Todo


def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')

    form = TodoForm()
    context = {
        'forms': form,
        'list': item_list,
        'title': 'TODO LIST',
        'to_update': "false",
    }
    print(context)
    return render(request, 'todo/index.html', context=context)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Item Deleted Successfully!!!")
    return redirect('todo')


def update(request, item_id):
    todo_item = Todo.objects.filter(id=item_id)
    if request.method == 'POST':
        u_form = TodoForm(request.POST, instance=todo_item[0])

        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your Todo has been Updated!')
            return redirect('todo')
    else:
        u_form = TodoForm(instance=todo_item[0])

    context = {
        'forms': u_form,
        'list': todo_item,
        'title': 'Update Todo',
        'to_update': "true",
    }
    return render(request, 'todo/index.html', context)