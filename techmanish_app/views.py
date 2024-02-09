from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import user_login

# Create your views here.


def home(request):
    return render(request, 'home.html')


def profile(request):
    # alldata = user_login.objects.all()
    data = {
        'name': "Manish",
        'job': "Devloper",
        'email': "ND772542@gmail.com"
    }
    all_data = user_login.objects.all()
    return render(request, 'profile.html',{'all_data':all_data})


def login(request):
    if request.method == 'POST':
        # userid = request.POST.get('id')
        userid = request.POST['id']
        # userpass = request.POST.get('password')
        userpass = request.POST['password']
        fatch = user_login(userid=userid, password=userpass)
        fatch.save()
        user_login.objects.all()
        
        
        return redirect(profile)
        # return HttpResponse("LOGIN SUCESSFULL............")
    else:
        return render(request, 'login.html')


def help(request):
    return render(request, 'help.html')


# this views for my potfolio

def intro(request):
    return render(request, "potfolio/introduction.html")


def profec(request):
    return render(request, "potfolio/profectional.html")


def persnal(request):
    return render(request, "potfolio/persnal.html")


def life_style(request):
    return render(request, "potfolio/life_style.html")


# profile update
# def editpage(request, pk):
#     # fetching the data
#     get_data = user_login.objects.get(userid=pk)
#     return render(request, "profile.html", {'key2': get_data})

# def update(request, pk):
#     udata = user_login.objects.get(id=pk)
#     udata = request.POST.get('userid')
#     udata.save()
#     return redirect(profile)
