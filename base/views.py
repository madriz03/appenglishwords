from django.shortcuts import render, redirect
# from django.http import HttpResponse #ADD FOR ME
from django.views.generic.list import ListView #ADD FOR ME
from django.views.generic.detail import DetailView #ADD FOR ME
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Task #ADD FOR ME
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
#Esta after line es para rentringir el acceso a una vista si el usuario no esta logueado
from django.contrib.auth.forms import UserCreationForm
#Esta linea after es para crear un formulario de registro

from django.contrib.auth import login

# Create your views here.
""" Nota importante el paranmetro LoginRequiredMixin se le pasa a todas las vistas que se quieran restringir en caso que el usuario no este logueado"""

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user: True

    def get_success_url(self):
        return reverse_lazy('tasks')




class RegisterPageView(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user: True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPageView, self).form_valid(form)


    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPageView, self).get(*args, **kwargs)

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'words' 
#El objeto paso de object_list a llamarse words

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['words'] = context['words'].filter(user=self.request.user)
        context['count'] = context['words'].filter(complete=False).count()

        #Add logic to method get, start here.
        search_input = self.request.GET.get('search-area') or ""
        if search_input:
            context['words'] = context['words'].filter(word__startswith=search_input)

        context['search_input'] = search_input
        return context



class TaskDetail(LoginRequiredMixin, DetailView):
   model = Task
   context_object_name = 'word'
   



class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['word', 'translation', 'sentence', 'complete']
    success_url = reverse_lazy('tasks')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)




class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['word', 'translation', 'sentence', 'complete']
    success_url = reverse_lazy('tasks')



class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'word'
    success_url = reverse_lazy('tasks')

"""Usa esta vista basada en clases que hereda de listviews no hace falta renderizar
A un templates indicandoselo, porque Django ya lo sabe y lo hara, eso si el te,plate 
debe tener el mismo nombre que el modelo."""