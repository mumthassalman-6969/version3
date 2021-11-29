from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def fnxyz(req):  
    return render(req,'file1.html')



