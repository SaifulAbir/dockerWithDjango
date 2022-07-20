from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def first_view(request):
    return HttpResponse('<h1>Django is cool and Docker Volumes are super awesome.</h1>')
