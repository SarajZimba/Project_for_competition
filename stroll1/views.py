from django.shortcuts import render, redirect
from .models import *
import json
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm

# Create your views here.
def index(request):
   
    dests = Destination.objects.all()
    context = {'dests': dests}
    return render(request, 'index.html', context)
def payment(request):
    return render(request, 'payment.html')
   
    # dests = Destination.objects.all()
    # context = {'dests': dests}

def search(request):
    # blogdatas = Blogs.objects.all()
    query = request.GET['query']
    if len(query) > 80:
        blogdatas= Blogs.objects.none()
    else:
        blogdatasname = Blogs.objects.filter(name__icontains=query)
        blogdatastag = Blogs.objects.filter(tag__icontains=query)

        blogdatas = blogdatasname.union(blogdatastag)
    # if blogdatas.count(datas) == 0:
    #     messages.warning(request, "No Search results found. Please refine your keyword.")
    context = {'blogdatas': blogdatas, 'query': query}
    return render(request, 'search.html', context)

def custom(request):
    data = json.loads(request.body)
    # print(data)
    # name = form['name']

    Custom.objects.create(
        name = data['form']['name'],
        destnation = data['form']['destination'],
        activity = data['form']['activity'],
        duration = data['form']['duration'],
        date = data['form']['date'],
    )
    print(data['form']['name'])


    return JsonResponse('Payment Complete', safe=False)

def loginPage(request):


    if request.method == 'POST':
        username = request.POST.get('username')
        print("username")
        print(username)
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.info(request, "Username or Password incorrect")
            return render(request, 'login.html')

    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
             form.save()
             user = form.cleaned_data.get('username')
             messages.success(request, 'Account was created for ' + user )
             return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
    

