from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

def index1(request):
    my_massege = "Hi! im ROYA.. wellcome to my site :)"
    context = {
        "t" : my_massege
    }
    return render (request,'challenge/pre.html',context)
    