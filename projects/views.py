from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return render(request, "index.html")


def dynamic(request, test="test"):
    return HttpResponse("<h1>Dynamic</h1><p>Here are my projects</p>" + str(test))
