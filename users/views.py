from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, 
                                  UpdateView, DeleteView, TemplateView)
from .forms import UserRegisterForm


def register_user(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
            # saves user to database
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
            # Flash message that appears for account creation confirmation and disappears
			messages.success(request, f'Welcome {username}, your account has been created!')
			return redirect('crm-home')
	else:
		form = UserRegisterForm()
		return render(request, 'users/register.html', {'form':form})

	return render(request, 'users/register.html', {'form':form})


"""class RegisterView(SuccessMessageMixin, FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm()
    success_url = reverse_lazy('login')
    
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form' : form})
    
    def post(self, request):
        form = self.form_class
        #form = UserRegisterForm(request.POST)
        if form.is_valid():
            # saves user to database
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Flash message that appears for account creation confirmation and disappears
            messages.success(request, f'Welcome {username}, your account has been created! You are now able to login.')
            return redirect('home')
        else:
            
        return render(request, self.template_name, {'form' : form})"""