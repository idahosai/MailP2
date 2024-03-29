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

    path('CreateContact3View/',views.CreateContact3View.as_view(),name='CreateContact3View/'),

    path('CreateSegmentIdToContactView/',views.CreateSegmentIdToContactView.as_view(),name='CreateSegmentIdToContactView/'),

    path('trackopenemails/<id>', views.trackopenemails, name='trackopenemails'),
    path('CreateEmailView/', views.CreateEmailView.as_view(), name='CreateEmailView'),
    path('CreateEmail2View/', views.CreateEmail2View.as_view(), name='CreateEmail2View'),

    path('GetIsRegisteredEmailApis/',views.GetIsRegisteredEmailApis.as_view(),name='GetIsRegisteredEmailApis/'),
    path('CreateRegisterAccountApis/',views.CreateRegisterAccountApis.as_view(),name='CreateRegisterAccountApis/'),

    path('CreateRegisterEmailSubscriberAccountApis/',views.CreateRegisterEmailSubscriberAccountApis.as_view(),name='CreateRegisterEmailSubscriberAccountApis/'),
    path('GetIsRegisteredEmailForSubscriberApis/',views.GetIsRegisteredEmailForSubscriberApis.as_view(),name='GetIsRegisteredEmailForSubscriberApis/'),

    path('checksigninsubscriberapi/',views.checksigninsubscriberapi.as_view(), name="checksigninsubscriberapi/"),
    

    path('GetRecoverPasswordApis/',views.GetRecoverPasswordApis.as_view(),name='GetRecoverPasswordApis/'),
    path('CreateAccountInformationApis/',views.CreateAccountInformationApis.as_view(),name='CreateAccountInformationApis/'),

    path('SearchedUsersApis/',views.SearchedUsersApis.as_view(),name='SearchedUsersApis/'),

    path('InboxApis/',views.InboxApis.as_view(),name='InboxApis/'),
    
    path('MessageApis/',views.MessageApis.as_view(),name='MessageApis/'),
    path('MessageAllApis/',views.MessageAllApis.as_view(), name='MessageAllApis/'),

    #path('post/',views.post,name="post/")
    path('playtemplate', views.playtemplate, name="playtemplate")
    
 ]