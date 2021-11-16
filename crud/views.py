from django import forms
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View, DetailView
from django.views.generic.list import ListView
from .models import Person, PersonModelForm

class IndexView(ListView):
    model = Person
    template_name = "crud/index.html"

class CreateView(TemplateView):
    template_name = "crud/create.html"

class PersonCreateView(CreateView):
    model = Person
    template_name = "crud/create.html"

    def post(self, request, *args, **kwargs):
        form = PersonModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return redirect('/')

class PersonDetailView(DetailView):
    model = Person
    template_name = "crud/create.html"

    def post(self, request, *args, **kwargs):
        form = PersonModelForm(request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
            return redirect('/')
        return redirect('/')


