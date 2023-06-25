from django.http import HttpResponse
from django.shortcuts import render
from . models import user_login

# Create your views here.

def home(request):
    return render(request,'home.html')

def profile(request):
    return render(request,'profile.html')

def login(request):
    if request.method=='POST':
        userid = request.POST.get('id')
        userpass = request.POST.get('password')
        fatch = user_login(userid=userid, password=userpass)
        fatch.save()
        user_login.objects.all()

        return HttpResponse("LOGIN SUCESSFULL............")
    else:
        return render(request,'login.html')

def help(request):
    return render(request,'help.html')