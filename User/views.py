from django.shortcuts import render
from .forms import AddJobForm, LoginForm
from .models import Jobs
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.viewsets import ModelViewSet
from .serializer import JobSerializer

# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            print("I am here")
            uname = request.POST.get('username')
            pwd = request.POST.get('password')
            print('un', uname, pwd)
            user_data = authenticate(request, username=uname, password=pwd)
            print('user', user_data)
            if user_data:
                login(request, user_data)
                return redirect('/')
        data = LoginForm()
        return render(request, 'User/login.html', context={'form': data})

def logout_page(request):
    logout(request)
    return redirect('login')

def home(request):
    jobs = Jobs.objects.all()
    if request.method == "GET":
        return render(request, 'User/home.html', {'jobs': jobs})
    else:
        print(request.POST)
        jobs= Jobs.objects.all()
        for q in jobs:
            if q.JobName in request.POST:
                if q.JobName == request.POST.get(q.JobName):
                    pass
        return render(request, 'User/result.html')
   # if request.user.is_authenticated:

def Jobs_Page(request):
    form_data= AddJobForm()
    return render(request, 'User/index.html', {'form': form_data})

class JobViewSet(ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer