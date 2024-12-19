# from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request): 
    if request.POST:
        todo123=request.POST.get("todo")
        todo321=request.POST.get("date")
        todo311=request.POST.get("course")
        obj=Todoitem(title1=todo123,title2=todo321,title3=todo311)
        obj.save()
        return redirect(index)
    data=Todoitem.objects.all()
    return render(request,"index.html",{"feeds":data})
# Create your views here.
