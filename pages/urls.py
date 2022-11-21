from django.urls import path 

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('registeraccount', views.registeraccount, name="registeraccount"),
    #name the fuction as signin and name the url as signin too
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('recoverpassword', views.recoverpassword, name="recoverpassword"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),

 ]