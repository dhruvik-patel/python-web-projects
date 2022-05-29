from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World From Index Function")
def temp(request):
    dict = { 'first_insert':'This is from template tag of first_app' }
    return render(request,'first_app/index.html',context=dict)
