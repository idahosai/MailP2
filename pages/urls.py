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
    #uidb64 is the user id coded in base 64, token to check if password is valid
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
    
    path('reset/<uidb64>/<token>', views.reset, name="reset"),
    path('resetpasswordconfirm', views.resetpasswordconfirm, name="resetpasswordconfirm"),
 
 ]