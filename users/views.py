from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already exist')
            return redirect('users:register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email already exist')
            return redirect('users:register')
        
        if password1 == password2:            
            user = User.objects.create_user(username = username, password = password1, email=email,first_name=first_name,last_name=last_name)
            user.save()
            messages.success(request,'Registration completed...')
            return redirect('/')
    else:
        return render(request,'users/register.html',{'title':'Register'})
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('users:login')
    else:
        return render(request,'users/login.html',{'title':'Login'})
    
    
def logout(request):
    auth.logout(request)
    return redirect('/')