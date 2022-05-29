from django.shortcuts import render
from apptwo.models import User
# Create your views here.

# index called directly from project's urls.py file
def index(request):
    return render(request, 'apptwo/index.html')

# users will be called from apptwo's urls.py file which is called when we Search '/users/' type string
def users(request):

    user_list = User.objects.order_by('first_name')
    user_dict = {'users' : user_list}
    return render(request , 'apptwo/users.html',context=user_dict)
