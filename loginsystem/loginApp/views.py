from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
def rigester(request):
    if request.method == "POST":
        user = request.POST['username']
        email = request.POST['email']
        passw1 = request.POST['password1']
        passw2 = request.POST['password2']
        if passw1 == passw2:
            if User.objects.filter(email= email).exists():
                messages.info( request,"Email aiready exits")
                return redirect('rigester')
            elif User.objects.filter(username =user).exists():
                messages.info(request,"Username aiready exits")
                return redirect('rigester')
            else:
                user = User.objects.create_user(username=user,email=email,password=passw1)
                messages.info(request, "Create new user")
                user.save()
                return redirect('login')
        else:
            messages.info(request,"password miss match")
            return redirect('rigester')
    return render(request, "rigester.html")
def login(request):
    if request.method == "POST":
        user = request.POST['username']
        passw1 = request.POST['password1']
        user = auth.authenticate(username=user,password=passw1)
        if user is not None:
            auth.login(request,user)
            return render(request,'login_User.html')
        else:
            messages.info(request,'creditional invaild')
            return redirect('login')
            return render(request,'login.html')
    else:
        return render(request, 'login.html')