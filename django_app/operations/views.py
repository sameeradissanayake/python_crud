from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def operations(request):
    template =loader.get_template('page.html')
    return HttpResponse(template.render())
