from django.shortcuts import render

# Create your views here.
def index(request):
    contex_dict = {'text':'Hello World','number':100}
    return render(request,'basic_app/index.html',contex_dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_template.html')
