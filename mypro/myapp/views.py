from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def index(request): 
    if request.POST:
        title=request.POST.get("data")
        print(title)
        return redirect("about")
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")