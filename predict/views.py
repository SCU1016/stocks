from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, Context, loader
import json

# Create your views here.
def index(request):
    data = {}
    data['title'] = 'stock predict'

    t = loader.get_template('index.html')
    c = Context({'data': data})
    return HttpResponse(t.render(c))