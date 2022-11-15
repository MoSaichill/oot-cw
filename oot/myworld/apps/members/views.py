from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Members

from django.template import loader

def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {'mymembers': mymembers}
    return HttpResponse(template.render(context, request))

def search(request):
    template = loader.get_template('search.html')
    namesearch = request.GET['search']
    mymembers = Members.objects.filter(name__icontains=namesearch)
    context = {'mymembers': mymembers}
    return HttpResponse(template.render(context, request))