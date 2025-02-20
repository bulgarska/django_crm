from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, 
                                  UpdateView, DeleteView, TemplateView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Record
from django.contrib import messages

class HomeView(ListView):
    template_name = 'crm/home.html'
    model = Record
    context_object_name = 'records'
    
class RecordDetailView(DetailView):
    model = Record
    
class RecordDeleteView(LoginRequiredMixin, DeleteView):
    model = Record
    success_url = '/'