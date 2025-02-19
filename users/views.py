from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import (ListView, DetailView, CreateView, 
                                  UpdateView, DeleteView, TemplateView)

class RegisterView(TemplateView):
    template_name = 'users/register.html'
