from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.



def home(request):
    w=works.objects.all()
    return render(request, "index.html" , {'workstodo':w})


def workinput(request):
    
    works(work=request.POST['work']).save()

    w=works.objects.all()
    return render(request, "index.html" ,{
        'webinput':works ,
        'workstodo': w,
    }) 


