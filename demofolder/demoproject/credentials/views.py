from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.
def register(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        passs = request.POST['pass']
        cpass = request.POST['cpass']
        if passs==cpass:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=passs)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request,"Password incorrect")
            return redirect('register')
    return render(request,"register.html")


def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passw = request.POST['pass']
        user = auth.authenticate(username=uname, password=passw)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')