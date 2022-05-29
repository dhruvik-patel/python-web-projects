from django.shortcuts import render
# from apptwo.models import User
from apptwo.forms import NewUser
# Create your views here.

# index called directly from project's urls.py file
def index(request):
    return render(request, 'apptwo/index.html')

# users will be called from apptwo's urls.py file which is called when we Search '/users/' type string
def users(request):
    form = NewUser()

    if request.method == 'POST':
        form = NewUser(request.POST)     # if u write 'post' in above line then use 'post' in this line instead of 'POST'

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("INVALID FORM")

    return render(request,'apptwo/users.html',{'form':form})
