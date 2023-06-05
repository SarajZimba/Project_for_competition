from django.shortcuts import render, redirect
from .models import *
import json
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm,ratingForm

from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user, allowed_users

from django.contrib.auth.models import Group

# from rest_framework.viewsets import ModelViewSet

# from .serializers import ProductSerializer, RatingSerializer

# from rest_framework.permissions import IsAuthenticated

# Create your views here.
# @login_required(login_url='login')

# @allowed_users(allowed_roles=['admin'])
def index(request):
   
    dests = Destination.objects.all()
    context = {'dests': dests}
    return render(request, 'index.html', context)

@login_required(login_url='login')
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

@unauthenticated_user
def loginPage(request):
        if request.method == 'POST':
            username = request.POST.get('username')
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

@unauthenticated_user
def register(request):
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user =form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name = 'customer')

                user.groups.add(group)

                Customer.objects.create(
                     user = user,
                     name= user.username,
                )

                messages.success(request, 'Account was created for ' + username )
                return redirect('login')
        context = {'form': form}
        return render(request, 'register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
     
     context = {}
     return render(request, 'userpage.html', context)


def ratingPage(request):
     form = ratingForm()

     if request.method == 'POST':
          form = ratingForm(request.POST)
          if form.is_valid:
               form.save()

     context = {'form': form}
     return render(request, 'rating.html', context)
# from rest framework




