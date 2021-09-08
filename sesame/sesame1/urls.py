from django.urls import path
from . import views

app_name='sesame1'

urlpatterns = [
    path('',views.index,name='index'),
    path('newpost/',views.newpost,name='newpost'),
    path('all/',views.all,name='all'),


]