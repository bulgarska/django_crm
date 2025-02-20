from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, 
                                  UpdateView, DeleteView, TemplateView)
from .models import Record

class HomeView(ListView):
    template_name = 'crm/home.html'
    model = Record
    context_object_name = 'records'
    
class RecordDetailView(DetailView):
    model = Record