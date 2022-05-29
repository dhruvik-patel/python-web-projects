from django.urls import path
from basic_app import views

app_name = 'basic_app'     # will be used in relative.html file

urlpatterns = [
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
]
