from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login


from django.urls import reverse_lazy

from .models import *
from .forms import SignupForm


class StudentList(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'base/home.html'
    

class StudentDetail(DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'base/information.html'


class Home(TemplateView):
    template_name = "base/home.html"


class Register(FormView):
    template_name = "base/register.html"
    form_class = SignupForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
            return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("home")
        return super(Register, self).get(*args, **kwargs)


class Login(LoginView):
    template_name = "base/login.html"
    fields = ['student_number', 'password']
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home")


class LessoneList(ListView):
    model = Lessone
    context_object_name = "lessones"
    template_name = "base/home_admin.html"


class LessoneDetail(DetailView):
    model = Lessone
    context_object_name = "lesoone"
    template_name = "lessone_detail.html"


class AddLessone_Admin(CreateView):
    model = Lessone
    template_name = "base/add_lessone.html"
    fields = "__all__"
    success_url = reverse_lazy("lessone-list") # elat estefade nakardan az reverse() ine ke in fun object mifreste va reverse ye str.


class UpdateLessone(UpdateView):
    model = Lessone
    template_nmae = "base/edit_lessone.html"
    fields = "__all__"
    success_url = reverse_lazy("lessone-list")
    

class DeleteLesoone(DeleteView):
    model = Lessone
    fields = "__all__"
    success_url = reverse_lazy("lessone-list")
    template_name = "/base/delete_lessone.html"