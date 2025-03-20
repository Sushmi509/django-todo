from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def login_(request):
    if request.method=='POST':
        username_data=request.POST['username']
        password_data=request.POST['password']
        print(username_data,password_data)
        all_userdata=authenticate(username=username_data,password=password_data)   # If the credentials are incorrect, authenticate returns None.
        if all is not None:
            login(request,all_userdata)
            return redirect('home')
        else:
            return render(request,'wrong.html')
    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        firstname_data=request.POST['firstname']
        lastname_data=request.POST['lastname']
        email_data=request.POST['email']
        username_data=request.POST['username']
        password_data=request.POST['password']
        print(username_data,password_data)

        u=User.objects.create(first_name=firstname_data,last_name=lastname_data,email=email_data,username=username_data,password=password_data)
        u.set_password(password_data)
        u.save()
        return redirect('login')
    return render(request,'register.html')

def logout_(request):
    logout(request)
    return redirect('logout')