from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
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


class LessonList(ListView):
    model = Lesson
    context_object_name = "lessons"
    template_name = "base/lesson_list.html"


class LessonDetail(DetailView):
    model = Lesson
    context_object_name = "lesson"
    template_name = "base/lesson_detail.html"


class AddLesson(CreateView):
    model = Lesson
    fields = "__all__"
    template_name = "base/add_lesson.html"
    success_url = reverse_lazy("lessons-list") # elat estefade nakardan az reverse() ine ke in fun object mifreste va reverse ye str.

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super(AddLessonAdmin, self).form_valid(form)


class UpdateLesson(UpdateView):
    model = Lesson
    template_name = "base/edit_lesson.html"
    fields = "__all__"
    success_url = reverse_lazy("lesson-list")


class DeleteLesson(DeleteView):
    model = Lesson
    fields = "__all__"
    success_url = reverse_lazy("lesson-list")
    template_name = "/base/delete_lesson.html"
