from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView
from app.models import *



class SchoolList(ListView):
    model=School
    context_object_name='allSO'
    template_name='app1\School_list.html'


class School_Detail(DetailView):
    model=School
    context_object_name='DOSI'
    template_name='app1\School_Detail.html'

