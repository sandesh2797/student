# i have created this file

from django.http import HttpResponse
def index(request):
    return HttpResponse ("helo world")