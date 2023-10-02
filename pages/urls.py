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

    path('accountinformation', views.accountinformation, name="accountinformation"),
    path('importsubscribers', views.importsubscribers, name="importsubscribers"),

    path('importsubscriber-table_load_up',views.table_load_up,name='importsubscriber-table_load_up'),
 
    path('importsubscribers_load_table',views.importsubscribers_load_table, name='importsubscribers_load_table'),
    path('matchtotable', views.matchtotable, name="matchtotable"),
    path('checksigninapi/',views.checksigninapi, name="checksigninapi/"),
    path('savecontactapi/',views.savecontactapi, name="savecontactapi/"),
    path('contactapi/',views.ContactApi.as_view(),name="contactapi/"),
    path('CreateContactView/',views.CreateContactView.as_view(),name="CreateContactView/"),
    path('CreateCustomfeildView/',views.CreateCustomfeildView.as_view(),name="CreateCustomfeildView/"),

    path('CreateCustomfeild2View/',views.CreateCustomfeild2View.as_view(),name='CreateCustomfeild2View/'),
    path('CreateContact2View/',views.CreateContact2View.as_view(),name='CreateContact2View/'),
    path('CreateSegmentView/',views.CreateSegmentView.as_view(),name='CreateSegmentView/'),
    path('CreateSegmentView2/',views.CreateSegmentView2.as_view(),name='CreateSegmentView2/'),

    path('CreateContact3View/',views.CreateContact3View.as_view(),name='CreateContact3View/'),

    path('CreateSegmentIdToContactView/',views.CreateSegmentIdToContactView.as_view(),name='CreateSegmentIdToContactView/'),

    #path('post/',views.post,name="post/")
    path('playtemplate', views.playtemplate, name="playtemplate")
    
 ]