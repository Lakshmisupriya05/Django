from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def home(request):
    return HttpResponse("country : India")
def firstpage(request):
    return HttpResponse("State : Andhra pradesh")
def secondpage(request):
    return HttpResponse("District : west Godavari")
def htmlpage(request):
    template = loader.get_template('student.html')
    return HttpResponse(template.render())