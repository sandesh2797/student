from django import http
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls.resolvers import _PATH_PARAMETER_COMPONENT_RE
from .models import myfit





# Create your views here.


def showindex(request):
    return render(request,'index.html')



def register(request):
    name=request.POST.get("cf-name")
    email=request.POST.get("cf-email")
    phone=request.POST.get("cf-phone")
    message=request.POST.get("cf-message")
    if request.method!="POST":
        return HttpResponse("method not allowed")
    else:
        
        myfit1=myfit()
        myfit1.name=name
        myfit1.email=email
        myfit1.phone_number=phone
        myfit1.message=message
        myfit1.save()
    
        return render(request,'index.html')





