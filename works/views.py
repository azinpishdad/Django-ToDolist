from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.



def home(request):
    w=works.objects.all()
    return render(request, "index.html" , {'workstodo':w})


def workinput(request):
    if "input" in request.POST:
        works(work=request.POST['work']).save()
    elif "delete" in request.POST:
        works.objects.filter(pk=request.POST['id']).delete()
    elif "update" in request.POST:
        works.objects.filter(pk=request.POST['id']).update(work=request.POST['work'])
    else:
        work="null"
        id="null"
    w=works.objects.all()
    return render(request, "index.html" ,{
        'webinput':works ,
        'workstodo': w,
    }) 


