
from django.urls import path
from . import views






urlpatterns = [
    path("", views.index, name="home"),
    path("custom", views.custom, name="custom"),
    path("<dest_id>/payment", views.payment, name="payment"),
    path("payment1", views.payment1, name="payment1"),
    path("search", views.search, name="search"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register", views.register, name="register"),
    path("userpage", views.userPage, name="userpage"),
    path("<dest_id>/rating", views.ratingPage, name="rating"),             
    path("<dest_id>/destination_details", views.destination_details, name="destination_details"),             
    path("maps/", views.maps, name="maps"),
    path("ktm/", views.mapsktm, name="mapsktm"),
    path("bkt/", views.mapsbkt, name="mapsbkt"),
    path("lpr/", views.mapslpr, name="mapslpr"),
    path("boudha/", views.mapsboudha, name="mapsboudha"),
    path("products/", views.products, name="products"),
    path("update_item/", views.update_item, name="update_item"),
    path("cart/", views.cart, name="cart"),
    path("viewPage/", views.viewPage, name="viewPage"),
    path("processorder", views.processOrder, name="processorder"),

    # user profile
    path("user-profile", views.UserProfile, name="user-profile"),
    path("<order_id>/showOrderitems", views.showOrderitems, name="showOrderitems"),


    # for destination order_khalti
    path("khalti-request", views.KhaltiRequest, name="khalti-request"),
    path("khalti-verify", views.KhaltiVerify, name="khalti-verify"),

    # for destination order_khalti
    path("esewa-request", views.EsewaRequest, name="esewa-request"),
    # path("esewa-verify", views.EsewaVerify, name="esewa-verify"),

    # for cart order
    path("khalti-request-cart", views.KhaltiRequestCart, name="khalti-request-cart"),
    path("khalti-verify-cart", views.KhaltiVerifyCart, name="khalti-verify-cart"),


]