from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')



def about(request):
    return HttpResponse('''<a href="https://www.tutorialspoint.com/questions_and_answers.htm"> excerise</a>''' )

def firstcap(request):
    return HttpResponse('hii first resopnse')

def lastcap(request):
    return HttpResponse('hii this is last')

def newline(request):
    return HttpResponse('hii this is new line')

def charcount(request):
    return HttpResponse("hii this is charcount <a href='/'>back</a>")
