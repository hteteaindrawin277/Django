from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Todoapp

def todo_list(request):
    all_data={'todo_list':Todoapp.objects.all()}
    return render(request,'todoapp/Todo_list.html',all_data)
def insert_todo(request:HttpRequest):
    todo=Todoapp(content=request.POST['content'])
    todo.save()
    return redirect('/todo/list')

def delete_todo_item(request,todo_id):
    todo_delete=Todoapp.objects.get(id=todo_id)
    todo_delete.delete()
    return redirect('/todo/list')