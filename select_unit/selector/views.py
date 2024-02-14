from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Student


class StudentList(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'base/home.html'
    

class StudentDetail(DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'base/information.html'
