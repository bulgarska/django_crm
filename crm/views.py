from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, 
                                  UpdateView, DeleteView, TemplateView)

class HomeView(TemplateView):
    template_name = 'crm/home.html'
