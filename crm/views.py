from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, 
                                  UpdateView, DeleteView, TemplateView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Record
from django.contrib import messages

class HomeView(LoginRequiredMixin, ListView):
    template_name = 'crm/home.html'
    model = Record
    context_object_name = 'records'
    
class RecordDetailView(LoginRequiredMixin, DetailView):
    model = Record
    
class RecordDeleteView(LoginRequiredMixin, DeleteView):
    model = Record
    success_url = '/'
    
class RecordCreateView(LoginRequiredMixin, CreateView):
    model = Record
    template_name_suffix = "_create_form"
    fields = ['first_name', 'last_name', 'email', 'phone', 
              'address', 'city', 'state', 'zipcode']
    
    def form_valid(self, form):
        return super().form_valid(form)

class RecordUpdateView(LoginRequiredMixin, UpdateView):
    model = Record
    # added to end of template name for distinguishment
    template_name_suffix = "_update_form"
    fields = ['first_name', 'last_name', 'email', 'phone', 
              'address', 'city', 'state', 'zipcode']
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    
    
    