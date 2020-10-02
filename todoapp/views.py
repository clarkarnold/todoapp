from django.shortcuts import render, get_object_or_404, redirect
from .models import ToDoItem
from .forms import ToDoItemForm


# Create your views here.
def todo_item_list(request):
    items = ToDoItem.objects.order_by('urgent','completed', '-date_created')
    return render(request, 'todoapp/todo_item_list.html', {'items':items})


def delete_item(request, pk):
    item = get_object_or_404(ToDoItem, pk=pk)
    item.delete()
    return redirect('todo_item_list')


def edit_item(request, pk):
    item = get_object_or_404(ToDoItem, pk=pk)
    if request.method == "POST":
        form = ToDoItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('todo_item_list')
    else:
        form = ToDoItemForm(instance=item)
    return render(request, 'todoapp/edit_item.html', {'form':form})


def new_item(request):
    if request.method == "POST":
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('todo_item_list')
    else:
        form = ToDoItemForm()
    return render(request, 'todoapp/new_item.html', {'form':form})


def mark_completed(request, pk):
    item = get_object_or_404(ToDoItem, pk=pk)
    item.complete()

    return redirect('todo_item_list')