import django
from  django.http import  HttpResponse


def index (request):
    return HttpResponse('Hello world')

def status (request):
    return HttpResponse('Ok world')
