# from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request): 
    if request.POST:
        todo123=request.POST.get("todo")
        obj=Todoitem(title=todo123)
        obj.save()
        return redirect(index)
    data=Todoitem.objects.all()
    return render(request,"index.html",{"feeds":data})
# Create your views here.
