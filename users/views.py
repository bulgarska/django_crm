from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, 
                                  UpdateView, DeleteView, TemplateView)
from .forms import UserRegisterForm


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm()
    success_url = reverse_lazy('login')
    
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class
        #form = UserRegisterForm(request.POST)
        if form.is_valid():
            # saves user to database
            form.save()
            username = form.cleaned_data.get('username')
            # Flash message that appears for account creation confirmation and disappears
            messages.success(request, f'Welcome {username}, your account has been created! You are now able to login.')
            return redirect('login')
        
        return render(request, self.template_name, {'form': form})