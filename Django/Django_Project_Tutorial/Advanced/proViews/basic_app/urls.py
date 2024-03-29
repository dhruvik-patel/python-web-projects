from django.urls import path
from basic_app import views
from django.conf.urls import url
app_name = 'basic_app'

urlpatterns = [
    path('',views.SchoolListView.as_view(),name='list'),
    url('^(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name='detail'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    url('^update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(),name='update'),
    url('^delete/(?P<pk>\d+)/$',views.SchoolDeleteView.as_view(),name='delete'),

]
