from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated Successfully')
                
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid User')
    else:
        form=LoginForm()
    
    data = {
        'form':form,
    }
    return render(request, 'account/login.html', data)


@login_required
def dashboard(request):
    data = {
        'section':'dashboard'
    }
    return render(request, 'account/dashboard.html', data)

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            data = {
                'new_user':new_user,
            }
            return render(request, 'account/register_done.html', data)
    else:
        user_form = UserRegistrationForm()
    data = {
            'user_form':user_form,
        }
    return render(request, 'account/register.html', data)   
    