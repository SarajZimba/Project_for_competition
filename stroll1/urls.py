from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("custom", views.custom, name="custom"),
    path("payment", views.payment, name="payment"),
    path("search", views.search, name="search"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register", views.register, name="register"),
               

]