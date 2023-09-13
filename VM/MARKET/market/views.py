from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

def home (request):
    if request.method == "GET":
        return render (request, "page/index.html")