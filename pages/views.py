import datetime
import http
import json
import re
from django.conf import settings
from django.shortcuts import render, redirect

from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from . tokens import generate_token


from pages.models import AttachedAll, AttachedForm, Attachedgroup, Attachedtag, Bulkimport, Form, Group, Staff, Tag, Contact, Customfeild, Attachedcustomfeild, Segment, Attachedsegment, JoinStaffContact, JoinStaffCustomfeild, Email, Attachedemail, Inbox, Inboxparticipants, Message
#from pages import settings
from django.core import serializers

from django.http import FileResponse, JsonResponse
from django.utils import timezone

from django.core.files.storage import default_storage

from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render
from rest_framework import generics
#from rest_framework.views import APIView
#from rest_framework.response import Response
from .serializers import CreateContactSerializer, CreateCustomfeildSerializer, CreateCustomfeild2Serializer, CreateContact2Serializer, CreateSegmentSerializer, CreateContactEmailSerializer, JoinStaffCustomfeildSerializer, JoinStaffContactSerializer, ShowSegmentSerializer, AttachedsegmentSerializer, GetIsRegisteredEmailApisSerializer, Staff2Serializer, Staff3Serializer, EmailSerializer, AttachedemailemailSerializer, User2Serializer, Inboxparticipants2InboxSerializer, MessageSerializer

from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer

from rest_framework.decorators import api_view



# Create your views here.
def playtemplate(request):
    return render(request, 'pages/playtemplate.html')

def index(request):
    return render(request, 'pages/index.html')
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #temporarily make log in
        #User.objects.create_user('malinda', 'malinda@sheridancollege.ca', 'malinda', last_login=timezone.now()).save()
        #User.objects.create_user('lydia', 'lydia.novak@sheridancollege.ca', 'lydia', last_login=timezone.now()).save()
        #User.objects.create_user('igbinosa', 'idahosai@sheridancollege.ca', 'igbinosa', last_login=timezone.now()).save()
        
        #u2 = User.objects.create_user('malinda', 'malinda@sheridancollege.ca', 'malinda', last_login=timezone.now())
        #u2.save()
  
        user = auth.authenticate(request, username=username, password=password)
        #will remove later
        #request.session['username'] = username

        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('index')
        
    else:
        #return render(request, 'pages/home.html')
        return render(request, 'pages/home.html')
    """

   

def registeraccount(request):

    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password']
        cpassword = request.POST['cpassword']
        industry = request.POST['industry']
        

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('index')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('index')
    
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('index')
        
        if password1 != cpassword:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('index')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('index')


        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname

        #this is whats stopping my loging in from working
        #for now we will leave it uncommented
        myuser.is_active = False

        myuser.is_staff = True
        myuser.save()
        staffuser = Staff.objects.create(userid=myuser.id ,username=username, firstname=fname, lastname=lname, emailaddress=email, industry=industry)
        staffuser.save()

        messages.success(request, "Your Account has been successfully created.")
        
        # Welcome Email
        subject = "Welcome to Mail Pinyata Login!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to Mail Pinyata!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You. \n"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        
        
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ Mail Pinyata Login!!"
        message2 = render_to_string('email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        email.fail_silently = True
        email.send()
        
        return redirect('signin')


    return render(request, 'pages/registeraccount.html')

def signup(request):
    return render(request, 'pages/index.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password) 
        #print(user.first_name)
        #print("******************************************************")
        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            #render(request, 'pages/index.html', {'fname': "yoyo"})
            return render(request, 'pages/index.html', {'fname': fname})
        else:
            messages.error(request, "Bad Credentials!") 
            return redirect('signin')

    return render(request, 'pages/signin.html')




def trackopenemails(request,id):
     if id:
     #if 'id' in request.GET:
        #do something with the id, which tells you that specific subscriber has opened the email.
        if Email.objects.get(id=id).opens is None:
            staffstuff = Email.objects.filter(id=id).update(opens=1)
        else:
            staffstuff = Email.objects.filter(id=id).update(opens=Email.objects.get(id=id).opens + 1)
            
            
            
     #do something to record that an email has been opened.
     #imagedata = open("static/img/mailppinyata.png", 'rb').read()
     imagedata = open('static/img/mailppinyata.png', 'rb')
     response = FileResponse(imagedata)

     return response
     #return http.HttpResponse(imagedata, mimetype="image/png")


class CreateEmailView(generics.ListCreateAPIView):
    serializer_class = EmailSerializer
    queryset = Email.objects.all()

    def post(self, request, pk=None):
            #if not self.request.session.exists(self.request.session.session_key):
            #    self.request.session.create()
            staffid = request.data['staffpk']
            name = request.data['name']
            numberofcontactssentto = request.data['numberofcontactssentto']
            dateofcreation = request.data['dateofcreation']
            subjecttitle = request.data['subjecttitle']
            
            emailuser = Email.objects.create(
            name = name,
            numberofcontactssentto = numberofcontactssentto,
            dateofcreation = dateofcreation,
            subjecttitle = subjecttitle,
            opens= 0,
            )
            emailuser.save()
            #i added this today
            staffuser = Staff.objects.get(id = int(staffid))
            #i added this today
            attachedemailuser = Attachedemail.objects.create(
                emailid = emailuser,
                staffid = staffuser,
                dateofattachement = dateofcreation
            )
            attachedemailuser.save()


            #make sure that username is unique for all who log in to the system
            #objectQuerySettag = Contact.objects.filter(id = contactuser.id)
            holder = Email.objects.get(id=emailuser.id)
            #holder.userid
            

            #userstaff2 = Staff.objects.get(id = staffuser.id)

            #querysetsandcf = JoinStaffCustomfeild.objects.filter(staffid = userstaff).only('customfeildid__id','customfeildid__name','customfeildid__customfeildintvalue','customfeildid__customfeildstringvalue','customfeildid__dateofcreation','customfeildid__lastcustomfeildupdate')
        
    
            serializer2 = EmailSerializer(holder,many=False)

            print("*******************")
            print(serializer2.data)
        
            return Response(serializer2.data)
            #print(objectQuerySettag)



class CreateEmail2View(generics.ListCreateAPIView):
    serializer_class = AttachedemailemailSerializer
    queryset = Attachedemail.objects.all()
    #renderer_classes = [TemplateHTMLRenderer]
    #template_name = 'contacts/contacts.html'

    
    #@api_view(['POST'])
    def get(self, request, *args, **kwargs):
        #if not self.request.session.exists(self.request.session.session_key):
        #    self.request.session.create()

        #id = request.data['id']
        #name = request.data['name']
        #customfeildintvalue = request.data['customfeildintvalue']
        #customfeildstringvalue = request.data['customfeildstringvalue']
        #dateofcreation = request.data['dateofcreation']
        #lastcustomfeildupdate = request.data['lastcustomfeildupdate']

        #g = Customfeild.objects.all()
        #this is new from today
        staffpk = request.GET.get('staffpk')
        staffuser = Staff.objects.get(id=staffpk)
        staffuser.save()
        queryset2 = Attachedemail.objects.filter(staffid = staffuser)
        serializer2 = AttachedemailemailSerializer(queryset2,many=True)

        #queryset = Contact.objects.all()
        #serializer = CreateContact2Serializer(queryset,many=True)
        
        
        #print(serializer.data)
        #print(list(dataB))
        #print(dataB)
        #json_object = json.loads(dataB)
        return Response(serializer2.data)



class SearchedUsersApis(generics.ListCreateAPIView):
    serializer_class = User2Serializer
    queryset = User.objects.all()
    #renderer_classes = [TemplateHTMLRenderer]
    #template_name = 'contacts/contacts.html'
    #@api_view(['POST'])
    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')
        
        queryset2 = User.objects.filter(first_name__startswith = search)
        serializer2 = User2Serializer(queryset2,many=True)

        return Response(serializer2.data)



class InboxApis(generics.ListCreateAPIView):
    serializer_class = Inboxparticipants2InboxSerializer
    queryset = Inboxparticipants.objects.all()
    #renderer_classes = [TemplateHTMLRenderer]
    #template_name = 'contacts/contacts.html'
    #@api_view(['POST'])
    def get(self, request, *args, **kwargs):
        userid = request.GET.get('userid')
        otheruserid = request.GET.get('otheruserid')


        

        b= Inboxparticipants.objects.filter(userid = userid, inboxid__userid = otheruserid)
        c= Inboxparticipants.objects.filter(userid = otheruserid, inboxid__userid = userid)

        print("111111111111111111111111111111")
        if b.count() > 0:
            #holduser = User.objects.get(id = userid)
            #holdotheruser = User.objects.get(id = otheruserid)
            queryset1 = Inboxparticipants.objects.filter(userid = userid, inboxid__userid = otheruserid)
            serializer1 = Inboxparticipants2InboxSerializer(queryset1,many=True)
            print("22222222222222222222222222222222")
            return Response(serializer1.data)
        
        if c.count() > 0:
            #holduser = User.objects.get(id = userid)
            #holdotheruser = User.objects.get(id = otheruserid)
            queryset2 = Inboxparticipants.objects.filter(userid = otheruserid, inboxid__userid = userid)
            serializer2 = Inboxparticipants2InboxSerializer(queryset2,many=True)
            print("333333333333333333333333333333333333")
            return Response(serializer2.data)
        
        print("44444444444444444444444444444444444444")
        holdotheruser = User.objects.get(id = otheruserid)

        inboxuser = Inbox.objects.create(userid = holdotheruser)
        inboxuser.save()


        holduser = User.objects.get(id = userid)


        Inboxparticipantsuser = Inboxparticipants.objects.create(inboxid = inboxuser, userid = holduser)
        Inboxparticipantsuser.save()

        a = Inboxparticipants.objects.filter(id = Inboxparticipantsuser.id)
        serializer3 = Inboxparticipants2InboxSerializer(a,many=True)

        print("555555555555555555555555555555555555555555555")
        return Response(serializer3.data)





class MessageApis(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    #renderer_classes = [TemplateHTMLRenderer]
    #template_name = 'contacts/contacts.html'

    
    #@api_view(['POST'])
    def post(self, request, pk=None):
        inboxid = request.data['inboxid']
        userid = request.data['userid']
        message = request.data['message']
        dateofcreation = request.data['dateofcreation']

        holdinbox = Inbox.objects.get(id = inboxid)
        holduser = User.objects.get(id = userid)


        messageuser = Message.objects.create(inboxid = holdinbox, userid = holduser, message = message, dateofcreation = dateofcreation)
        messageuser.save()

        a = Message.objects.filter(id = messageuser.id)
        serializer3 = MessageSerializer(a,many=True)

        return Response(serializer3.data)



class MessageAllApis(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    #renderer_classes = [TemplateHTMLRenderer]
    #template_name = 'contacts/contacts.html'
    #@api_view(['POST'])
    def get(self, request, *args, **kwargs):
        inboxid = request.GET.get('inboxid')
        holdinbox = Inbox.objects.get(id = inboxid)

        a = Message.objects.filter(inboxid = holdinbox.id).order_by("-dateofcreation")
        serializer3 = MessageSerializer(a,many=True)

        return Response(serializer3.data)





#@api_view(['POST'])
def checksigninapi(request):
    if request.method == 'GET':
        #username = request.POST['username']
        #password = request.POST['password']

        username = request.GET['username']
        password = request.GET['password']
        #username = "iggy"
        #password = "Iggyboy4"

        user = authenticate(request, username=username, password=password) 
        #print(user.first_name)
        #print("******************************************************")
        if user is not None:
            #login(request, user)
            #fname = user.first_name
            #messages.success(request, "Logged In Sucessfully!!")
            #render(request, 'pages/index.html', {'fname': "yoyo"})
            #return render(request, 'pages/index.html', {'fname': fname})
        
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            #objectQuerySettag = Attachedtag.objects.filter(tagid__type = "Purchase").select_related("tagid")

            #make sure that username is unique for all who log in to the system
            objectQuerySettag = Staff.objects.filter(username = username)
            #print(objectQuerySettag)
            dataB = serializers.serialize("json", objectQuerySettag, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['id','userid', 'username', 'firstname','lastname','emailaddress','industry'])
            #print(list(dataB))
            json_object = json.loads(dataB)
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            response = {
            'istrue': "true",
            'Staff': dataB
            }

            #return JsonResponse(response)
            return JsonResponse(json_object,safe=False)
        else:
            #messages.error(request, "Bad Credentials!") 
            #return redirect('signin')
            response = {
            'istrue': "false",
            'Staff': "is null"

            }
            dataB=[]
            #return JsonResponse(response)
            return JsonResponse(dataB,safe=False)

    response = {
            'istrue': "unknown",
            'Staff': "is null"
            }
    dataB=[]
    #return JsonResponse(response)
    return JsonResponse(dataB,safe=False)
    #return render(request, 'pages/signin.html')






class checksigninsubscriberapi(generics.ListCreateAPIView):
    serializer_class = User2Serializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):

        if request.method == 'GET':
            #username = request.POST['username']
            #password = request.POST['password']

            username = request.GET['username']
            password = request.GET['password']
            #username = "iggy"
            #password = "Iggyboy4"

            user = authenticate(request, username=username, password=password) 
            #print(user.first_name)
            #print("******************************************************")
            if user is not None:
                #login(request, user)
                #fname = user.first_name
                #messages.success(request, "Logged In Sucessfully!!")
                #render(request, 'pages/index.html', {'fname': "yoyo"})
                #return render(request, 'pages/index.html', {'fname': fname})
            
                print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
                #objectQuerySettag = Attachedtag.objects.filter(tagid__type = "Purchase").select_related("tagid")

                #make sure that username is unique for all who log in to the system


                userhere = User.objects.filter(username = username)

        
                serializer2 = User2Serializer(userhere,many=True)

                print("*******************")
                print(serializer2.data)
       
                return Response(serializer2.data)


            else:
                #messages.error(request, "Bad Credentials!") 
                #return redirect('signin')
                
                dataB=[]
                #return JsonResponse(response)
                return Response(dataB)

        
        dataB=[]
        #return JsonResponse(response)
        return Response(dataB)
        #return render(request, 'pages/signin.html')







#class CreateContactView(APIView):
#class CreateContactView(viewsets.ModelViewSet):
#@csrf_exempt
#generics.ListCreateAPIView is the one that works it seems
class CreateContactView(generics.ListCreateAPIView):
    serializer_class = CreateContactSerializer
    queryset = Contact.objects.all()
    #renderer_classes = [TemplateHTMLRenderer]
    #template_name = 'contacts/contacts.html'

    
    #@api_view(['POST'])
    def post(self, request, pk=None):
        #if not self.request.session.exists(self.request.session.session_key):
        #    self.request.session.create()
        datejoined = request.data['datejoined']
        notes = request.data['notes']
        emailaddress= request.data['emailaddress']
        firstname = request.data['firstname']
        lastname = request.data['lastname']
        jobtitle = request.data['jobtitle']
        company = request.data['company']
        mobilephone = request.data['mobilephone']
        workphone = request.data['workphone']
        country = request.data['country']
        stateprovince = request.data['stateprovince']
        city = request.data['city']
        address = request.data['address']
        zip = request.data['zip']
        website = request.data['website']
        addmethod = request.data['addmethod']

        #just added this today
        staffpk= request.data['staffpk']

        contactuser = Contact.objects.create(
            lifetimevalue = 0,
            datejoined = datejoined,
            notes = notes,
            emailaddress= emailaddress,
            firstname = firstname,
            lastname = lastname,
            jobtitle = jobtitle,
            company = company,
            mobilephone = mobilephone,
            workphone = workphone,
            country = country,
            stateprovince = stateprovince,
            city = city,
            address = address,
            zip = zip,
            website = website,
            addmethod = addmethod)
        contactuser.save()
        #i added this today
        staffuser = Staff.objects.get(id = staffpk)
        #i added this today
        joinstaffcontactuser = JoinStaffContact.objects.create(
            contactid = contactuser,
            staffid = staffuser
        )
        joinstaffcontactuser.save()


            #make sure that username is unique for all who log in to the system
        objectQuerySettag = Contact.objects.filter(id = contactuser.id)
        #print(objectQuerySettag)
        dataB = serializers.serialize("json", objectQuerySettag, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=[
        'id',
        'status',
        'lifetimevalue', 
        'datejoined', 
        'notes',
        'emailaddress',
        'firstname',
        'lastname',
        'jobtitle',
        'company',
        'mobilephone',
        'workphone',
        'country',
        'stateprovince',
        'city',
        'address',
        'zip',
        'website',
        'stopmethod',
        'confirmquestionmark',
        'addmethod',
        'signupsource',
        'totalreviewsleft',
        'lastemailratingdone'
        ])
        #print(list(dataB))
        #print(dataB)
        json_object = json.loads(dataB)
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        

        #return JsonResponse(response)
        return Response(json_object)



class GetIsRegisteredEmailApis(generics.ListCreateAPIView):
    serializer_class = GetIsRegisteredEmailApisSerializer
    queryset = User.objects.all()
    

    def get(self, request, *args, **kwargs):
        
        emailaddress = request.GET.get('emailaddress')

        #objects.get doesn't return empty result but filter does
        #isn't this supposed to be staff?
        #***************************************************************************************************************************
        usercontact = User.objects.filter(email = emailaddress)

        print("*******************here i am ********************************")

        if usercontact:
            serializer2 = GetIsRegisteredEmailApisSerializer(usercontact,many=True)

            print("*******************")
            print(serializer2.data)
       
            return Response(serializer2.data)
        
        else:
            response = {
            }
            dataB=[]
            return Response(dataB)
           





class GetIsRegisteredEmailForSubscriberApis(generics.ListCreateAPIView):
    serializer_class = GetIsRegisteredEmailApisSerializer
    queryset = Contact.objects.all()

    def get(self, request, *args, **kwargs):
        
        emailaddress = request.GET.get('emailaddress')

        #objects.get doesn't return empty result but filter does
        #isn't this supposed to be staff?
        #***************************************************************************************************************************
        usercontact = Contact.objects.filter(emailaddress = emailaddress)

        if usercontact:
            serializer2 = GetIsRegisteredEmailApisSerializer(usercontact,many=True)

            print("*******************")
            print(serializer2.data)
       
            return Response(serializer2.data)
        
        else:
            response = {
            }
            dataB=[]
            return Response(dataB)
           


  
        


class CreateRegisterAccountApis(generics.ListCreateAPIView):
    serializer_class = Staff2Serializer
    queryset = Staff.objects.all()

    def post(self, request, pk=None):
        username = request.data['username']
        firstname = request.data['firstname']
        lastname = request.data['lastname']
        emailaddress = request.data['emailaddress']
        password = request.data['password']
        industry = request.data['industry']

        myuser = User.objects.create_user(username, emailaddress, password)
        myuser.first_name = firstname
        myuser.last_name = lastname

        #this is whats stopping my loging in from working
        #for now we will leave it uncommented
        myuser.is_active = False

        myuser.is_staff = True
        myuser.save()
        staffuser = Staff.objects.create(userid=myuser.id ,username=username, firstname=firstname, lastname=lastname, emailaddress=emailaddress, industry=industry)
        staffuser.save()

        #messages.success(request, "Your Account has been successfully created.")
        
        # Welcome Email
        subject = "Welcome to Mail Pinyata Login!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to Mail Pinyata!! \nThank you for visiting our website\n"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ Mail Pinyata Login!!"
        message2 = render_to_string('email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        email.fail_silently = True
        email.send()
        


        userstaff2 = Staff.objects.get(id = staffuser.id)

        #querysetsandcf = JoinStaffCustomfeild.objects.filter(staffid = userstaff).only('customfeildid__id','customfeildid__name','customfeildid__customfeildintvalue','customfeildid__customfeildstringvalue','customfeildid__dateofcreation','customfeildid__lastcustomfeildupdate')
       
   
        serializer2 = Staff2Serializer(userstaff2,many=False)

        print("*******************")
        print(serializer2.data)
       
        return Response(serializer2.data)
    
        


class CreateRegisterEmailSubscriberAccountApis(generics.ListCreateAPIView):
    serializer_class = User2Serializer
    queryset = User.objects.all()

    def post(self, request, pk=None):
        username = request.data['username']
        firstname = request.data['firstname']
        lastname = request.data['lastname']
        emailaddress = request.data['emailaddress']
        password = request.data['password']
     

        myuser = User.objects.create_user(username, emailaddress, password)
        myuser.first_name = firstname
        myuser.last_name = lastname

        #this is whats stopping my loging in from working
        #for now we will leave it uncommented
        myuser.is_active = True

        myuser.is_staff = False
        myuser.save()

        userstaff2 = User.objects.get(email = emailaddress)
        #querysetsandcf = JoinStaffCustomfeild.objects.filter(staffid = userstaff).only('customfeildid__id','customfeildid__name','customfeildid__customfeildintvalue','customfeildid__customfeildstringvalue','customfeildid__dateofcreation','customfeildid__lastcustomfeildupdate')
        serializer2 = User2Serializer(userstaff2,many=False)

        print("*******************")
        print(serializer2.data)
       
        return Response(serializer2.data)
    
       




class GetRecoverPasswordApis(generics.ListCreateAPIView):
    serializer_class = Staff2Serializer
    queryset = Staff.objects.all()

    def get(self, request, *args, **kwargs):

        user_email = request.GET.get('emailaddress')
        
        associated_user = User.objects.filter(email=user_email).first()

        

        if associated_user:
            current_site = get_current_site(request)
            email_subject = "Password Reset request"
            #the file which will hold the message being sent
            message2 = render_to_string('templateactivateaccount.html',{
            
            'name': associated_user.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
            'token': generate_token.make_token(associated_user)
            })
            email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [associated_user.email],
            )
            email.fail_silently = True

            email.send()

            userstaff2 = Staff.objects.get(emailaddress = user_email)
            serializer2 = Staff2Serializer(userstaff2,many=False)

            print("*******************")
            print(serializer2.data)
        
            return Response(serializer2.data)


    


    






class CreateCustomfeildView(generics.ListCreateAPIView):
    serializer_class = CreateCustomfeildSerializer
    queryset = Customfeild.objects.all()
    #renderer_classes = [TemplateHTMLRenderer]
    #template_name = 'contacts/contacts.html'

    
    #@api_view(['POST'])
    def post(self, request, pk=None):
        #if not self.request.session.exists(self.request.session.session_key):
        #    self.request.session.create()
        contactpk = request.data['contactpk']

        name = request.data['name']
        customfeildintvalue = request.data['customfeildintvalue']
        customfeildstringvalue = request.data['customfeildstringvalue']
        dateofcreation = request.data['dateofcreation']
        lastcustomfeildupdate = request.data['lastcustomfeildupdate']

        staffpk= request.data['staffpk']

       



        customfeilduser = Customfeild.objects.create(
            name = name,
            customfeildintvalue = (int)(customfeildintvalue),
            customfeildstringvalue = customfeildstringvalue,
            dateofcreation = dateofcreation,
            lastcustomfeildupdate = lastcustomfeildupdate)
        customfeilduser.save()


        contactuser = Contact.objects.get(id = contactpk)

        attachedcustomfeilduser = Attachedcustomfeild.objects.create(
            dateofattachement = datetime.datetime.now(),
            contactid = contactuser,
            customfeildid = customfeilduser
        )
        attachedcustomfeilduser.save()

        staffuser = Staff.objects.get(id = staffpk)

        attachedAlluser = AttachedAll.objects.create(
            dateofattachement = datetime.datetime.now(),
            attachedcustomfeildid = attachedcustomfeilduser,
            staffid = staffuser
        )
        attachedAlluser.save()


        #i added this today
        joinstaffcustomfeilduser = JoinStaffCustomfeild.objects.create(
            customfeildid = customfeilduser,
            staffid = staffuser
        )
        joinstaffcustomfeilduser.save()

            #make sure that username is unique for all who log in to the system
        objectQuerySettag = Contact.objects.filter(id = contactpk)
        #print(objectQuerySettag)
        dataB = serializers.serialize("json", objectQuerySettag, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=[
        'id',
        'status',
        'lifetimevalue', 
        'datejoined', 
        'notes',
        'emailaddress',
        'firstname',
        'lastname',
        'jobtitle',
        'company',
        'mobilephone',
        'workphone',
        'country',
        'stateprovince',
        'city',
        'address',
        'zip',
        'website',
        'stopmethod',
        'confirmquestionmark',
        'addmethod',
        'signupsource',
        'totalreviewsleft',
        'lastemailratingdone'
        ])
        #print(list(dataB))
        #print(dataB)
        json_object = json.loads(dataB)
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        

        #return JsonResponse(response)
        return Response(json_object)
    

#newwwwwwwwwwwwwwwwwwwwwwww 11111111111111111
class CreateCustomfeild2View(generics.ListCreateAPIView):
    #serializer_class = CreateCustomfeild2Serializer
    #queryset = Customfeild.objects.all()

    serializer_class = JoinStaffCustomfeildSerializer
    queryset = JoinStaffCustomfeild.objects.all()
    

    
    #@api_view(['POST'])
    def get(self, request, *args, **kwargs):
        #if not self.request.session.exists(self.request.session.session_key):
        #    self.request.session.create()

        #id = request.data['id']
        #name = request.data['name']
        #customfeildintvalue = request.data['customfeildintvalue']
        #customfeildstringvalue = request.data['customfeildstringvalue']
        #dateofcreation = request.data['dateofcreation']
        #lastcustomfeildupdate = request.data['lastcustomfeildupdate']

        #g = Customfeild.objects.all()

        

        staffpk = request.GET.get('staffpk')

        userstaff = Staff.objects.get(id = staffpk)

        querysetsandcf = JoinStaffCustomfeild.objects.filter(staffid = userstaff).only('customfeildid__id','customfeildid__name','customfeildid__customfeildintvalue','customfeildid__customfeildstringvalue','customfeildid__dateofcreation','customfeildid__lastcustomfeildupdate')
        #select_related("customfeildid").prefetch_related('customfeildid')
        #print(querysetsandcf.values('customfeildid__id','customfeildid__name','customfeildid__customfeildintvalue','customfeildid__customfeildstringvalue','customfeildid__dateofcreation','customfeildid__lastcustomfeildupdate'))
        #print(str(querysetsandcf))
        #print(querysetsandcf)

        #dataB = serializers.serialize("json", querysetsandcf, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=[
        #'customfeildid',
        #])
        
        #'customfeildid__id',
        #'customfeildid__name',
        #'customfeildid__customfeildintvalue',
        #'customfeildid__customfeildstringvalue',
        #'customfeildid__dateofcreation',
        #'customfeildid__lastcustomfeildupdate'
        #print(dataB)
        #print(json.dumps(dataB))

        #queryset = Customfeild.objects.all()
        #serializer = CreateCustomfeild2Serializer(querysetsandcf,many=True)
        serializer2 = JoinStaffCustomfeildSerializer(querysetsandcf,many=True)

        print("*******************")
        print(serializer2.data)
        #print(list(dataB))
        #print(dataB)
        #json_object = json.loads(dataB)
        #return Response(serializer.data)
        return Response(serializer2.data)
        #JsonResponse(dataB,safe=False)

#newwwwwwwwwwwwwwwwwwwwwwwwww 22222222222222222
class CreateContact2View(generics.ListCreateAPIView):
    serializer_class = JoinStaffContactSerializer
    queryset = JoinStaffContact.objects.all()
    #renderer_classes = [TemplateHTMLRenderer]
    #template_name = 'contacts/contacts.html'

    
    #@api_view(['POST'])
    def get(self, request, *args, **kwargs):
        #if not self.request.session.exists(self.request.session.session_key):
        #    self.request.session.create()

        #id = request.data['id']
        #name = request.data['name']
        #customfeildintvalue = request.data['customfeildintvalue']
        #customfeildstringvalue = request.data['customfeildstringvalue']
        #dateofcreation = request.data['dateofcreation']
        #lastcustomfeildupdate = request.data['lastcustomfeildupdate']

        #g = Customfeild.objects.all()
        #this is new from today
        staffpk = request.GET.get('staffpk')
        staffuser = Staff.objects.get(id=staffpk)
        staffuser.save()
        queryset2 = JoinStaffContact.objects.filter(staffid = staffuser)
        serializer2 = JoinStaffContactSerializer(queryset2,many=True)

        #queryset = Contact.objects.all()
        #serializer = CreateContact2Serializer(queryset,many=True)
        
        
        #print(serializer.data)
        #print(list(dataB))
        #print(dataB)
        #json_object = json.loads(dataB)
        return Response(serializer2.data)


    def post(self, request):
        id = request.data['id']
        name = request.data['name']
        customfeildstringvalue = request.data['customfeildstringvalue']
        dateofcreation = request.data['dateofcreation']
        lastcustomfeildupdate = request.data['lastcustomfeildupdate']

        queryset = Customfeild.objects.get(id=id)
        queryset.name = name
        queryset.customfeildstringvalue= customfeildstringvalue
        queryset.dateofcreation=dateofcreation
        queryset.lastcustomfeildupdate = lastcustomfeildupdate
        queryset.save()

        queryset2 = Customfeild.objects.filter(id=id)
        serializer = CreateSegmentSerializer(queryset2,many=True)
        print(serializer.data)
        #print(list(dataB))
        #print(dataB)
        #json_object = json.loads(dataB)
        return Response(serializer.data)


class CreateSegmentView(generics.ListCreateAPIView):
    serializer_class = CreateSegmentSerializer
    queryset = Segment.objects.all()
    #renderer_classes = [TemplateHTMLRenderer]
    #template_name = 'contacts/contacts.html'

    
    #@api_view(['POST'])
    def get(self, request, *args, **kwargs):
        #if not self.request.session.exists(self.request.session.session_key):
        #    self.request.session.create()
        #id = request.data['id']
        #name = request.data['name']
        #customfeildintvalue = request.data['customfeildintvalue']
        #customfeildstringvalue = request.data['customfeildstringvalue']
        #dateofcreation = request.data['dateofcreation']
        #lastcustomfeildupdate = request.data['lastcustomfeildupdate']
        #g = Customfeild.objects.all()
        staffpk = request.GET.get('staffpk')

        staffuser = Staff.objects.get(id=staffpk)
        
        queryset2 = Attachedsegment.objects.filter(staffid = staffuser)
        serializer2 = AttachedsegmentSerializer(queryset2,many=True)

        #queryset = Segment.objects.all()
        #serializer = CreateSegmentSerializer(queryset,many=True)
        
        
        #print(serializer.data)
        #print(list(dataB))
        #print(dataB)
        #json_object = json.loads(dataB)
        return Response(serializer2.data)


    def post(self, request):
        #if not self.request.session.exists(self.request.session.session_key):
        #    self.request.session.create()
        

        name = request.data['name']
        dateone = request.data['dateone']
        datetwo = request.data['datetwo']
        dateofcreation = request.data['dateofcreation']
        staffpk = request.data['staffpk']


        segmentuser = Segment.objects.create(
            name = name,
            dateone = dateone,
            datetwo = datetwo,
            dateofcreation = dateofcreation)
        segmentuser.save()

        #contactuser = Contact.objects.get(id = contactpk)
    

        staffuser = Staff.objects.get(id=staffpk)
        #just added this to test if its cus of this
        staffuser.save()
        attachedsegmentuser = Attachedsegment.objects.create(
            dateofattachement = datetime.datetime.now(),
            segmentid = segmentuser,
            staffid = staffuser
        )
        attachedsegmentuser.save()

        queryset2 = Segment.objects.filter(id = segmentuser.id)
        serializer2 = CreateSegmentSerializer(queryset2,many=True)
        print(serializer2.data)
        #print(list(dataB))
        #print(dataB)
        #json_object = json.loads(dataB)
        return Response(serializer2.data)







class CreateContact3View(generics.ListCreateAPIView):
    serializer_class = JoinStaffContactSerializer
    queryset = JoinStaffContact.objects.all()
    #renderer_classes = [TemplateHTMLRenderer]
    #template_name = 'contacts/contacts.html'

    #wronge datatype, its supposed to be get
    def get(self, request, *args, **kwargs):
        #date1 = request.data['date1']
        date1 = request.GET.get('date1')
        #date2 = request.data['date2']
        date2 = request.GET.get('date2')
        #i just added this today
        #staffpk = request.data['staffpk']
        staffpk = request.GET.get('staffpk')

        staffuser = Staff.objects.get(id=staffpk)
        
        queryset2 = JoinStaffContact.objects.filter(contactid__datejoined__gte=date1, contactid__datejoined__lte=date2, staffid = staffuser)
        serializer2 = JoinStaffContactSerializer(queryset2,many=True)
        #queryset2 = Contact.objects.filter(datejoined__gte=date1, datejoined__lte=date2)
        #serializer = CreateContact2Serializer(queryset2,many=True)
        print(serializer2.data)
        #print(list(dataB))
        #print(dataB)
        #json_object = json.loads(dataB)
        return Response(serializer2.data)


class CreateSegmentIdToContactView(generics.ListCreateAPIView):
    serializer_class = CreateContactEmailSerializer
    queryset = Contact.objects.all()
    #renderer_classes = [TemplateHTMLRenderer]
    #template_name = 'contacts/contacts.html'

    def post(self, request):
        id = request.data['id']
        
        queryset = Segment.objects.get(id = id)
        

        queryset2 = Contact.objects.filter(datejoined__gte=queryset.dateone, datejoined__lte=queryset.datetwo)
        serializer = CreateContactEmailSerializer(queryset2,many=True)
        print(serializer.data)
        #print(list(dataB))
        #print(dataB)
        #json_object = json.loads(dataB)
        return Response(serializer.data)



class ContactApi(APIView):
    def get(self, request):
        objectQuerySettag = Contact.objects.all().values()
        dataB = serializers.serialize("json", objectQuerySettag, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=[
        'id',
        'status',
        'lifetimevalue', 
        'datejoined', 
        'notes',
        'emailaddress',
        'firstname',
        'lastname',
        'jobtitle',
        'company',
        'mobilephone',
        'workphone',
        'country',
        'stateprovince',
        'city',
        'address',
        'zip',
        'website',
        'stopmethod',
        'confirmquestionmark',
        'addmethod',
        'signupsource',
        'totalreviewsleft',
        'lastemailratingdone'
        ])
        json_object = json.loads(dataB)
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        #return JsonResponse(response)
        return Response(json_object,safe=False)
        #return Response

    def post(self, request):
        datejoined = request.data['datejoined']
        notes = request.data['notes']
        emailaddress= request.data['emailaddress']
        firstname = request.data['firstname']
        lastname = request.data['lastname']
        jobtitle = request.data['jobtitle']
        company = request.data['company']
        mobilephone = request.data['mobilephone']
        workphone = request.data['workphone']
        country = request.data['country']
        stateprovince = request.data['stateprovince']
        city = request.data['city']
        address = request.data['address']
        zip = request.data['zip']
        website = request.data['website']
        addmethod = request.data['addmethod']
        
        contactuser = Contact.objects.create(
            datejoined = datejoined,
            notes = notes,
            emailaddress= emailaddress,
            firstname = firstname,
            lastname = lastname,
            jobtitle = jobtitle,
            company = company,
            mobilephone = mobilephone,
            workphone = workphone,
            country = country,
            stateprovince = stateprovince,
            city = city,
            address = address,
            zip = zip,
            website = website,
            addmethod = addmethod)
        contactuser.save()

        #make sure that username is unique for all who log in to the system
        objectQuerySettag = Contact.objects.filter(id = contactuser.id)
        #print(objectQuerySettag)
        dataB = serializers.serialize("json", objectQuerySettag, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=[
        'id',
        'status',
        'lifetimevalue', 
        'datejoined', 
        'notes',
        'emailaddress',
        'firstname',
        'lastname',
        'jobtitle',
        'company',
        'mobilephone',
        'workphone',
        'country',
        'stateprovince',
        'city',
        'address',
        'zip',
        'website',
        'stopmethod',
        'confirmquestionmark',
        'addmethod',
        'signupsource',
        'totalreviewsleft',
        'lastemailratingdone'
        ])
        #print(list(dataB))
        json_object = json.loads(dataB)
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        

        #return JsonResponse(response)
        return Response(json_object,safe=False)
        #return ContactApi(obj['yo'], obj['do'])



"""
def savecontactapi(request):
    datejoined = request.data['datejoined']
    notes = request.data['notes']
    emailaddress= request.data['emailaddress']
    firstname = request.data['firstname']
    lastname = request.data['lastname']
    jobtitle = request.data['jobtitle']
    company = request.data['company']
    mobilephone = request.data['mobilephone']
    workphone = request.data['workphone']
    country = request.data['country']
    stateprovince = request.data['stateprovince']
    city = request.data['city']
    address = request.data['address']
    zip = request.data['zip']
    website = request.data['website']
    addmethod = request.data['addmethod']

    contactuser = Contact.objects.create(
        datejoined = datejoined,
        notes = notes,
        emailaddress= emailaddress,
        firstname = firstname,
        lastname = lastname,
        jobtitle = jobtitle,
        company = company,
        mobilephone = mobilephone,
        workphone = workphone,
        country = country,
        stateprovince = stateprovince,
        city = city,
        address = address,
        zip = zip,
        website = website,
        addmethod = addmethod)
    contactuser.save()

    #make sure that username is unique for all who log in to the system
    objectQuerySettag = Contact.objects.filter(id = contactuser.id)
    #print(objectQuerySettag)
    dataB = serializers.serialize("json", objectQuerySettag, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=[
    'id',
    'status',
    'lifetimevalue', 
    'datejoined', 
    'notes',
    'emailaddress',
    'firstname',
    'lastname',
    'jobtitle',
    'company',
    'mobilephone',
    'workphone',
    'country',
    'stateprovince',
    'city',
    'address',
    'zip',
    'website',
    'stopmethod',
    'confirmquestionmark',
    'addmethod',
    'signupsource',
    'totalreviewsleft',
    'lastemailratingdone'
    ])
    json_object = json.loads(dataB)
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    

    return JsonResponse(json_object,safe=False)
"""



#@api_view(['POST'])
@csrf_exempt
def savecontactapi(request):
    if request.method == 'POST':
    #arrCustomfeilds = request.POST.getlist('arrCustomfeilds[]')
    #print("arrcustomfeild is " + arrCustomfeilds)
        datejoined = request.POST['datejoined']
        notes = request.POST['notes']
        emailaddress= request.POST['emailaddress']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        jobtitle = request.POST['jobtitle']
        company = request.POST['company']
        mobilephone = request.POST['mobilephone']
        workphone = request.POST['workphone']
        country = request.POST['country']
        stateprovince = request.POST['stateprovince']
        city = request.POST['city']
        address = request.POST['address']
        zip = request.POST['zip']
        website = request.POST['website']
        addmethod = request.POST['addmethod']
    #for i in arrCustomfeilds:
    #    print("arrcustomfeild inside is " + i)
    #for i in range(len(arrCustomfeilds)):
    #    print("arrcustomfeild inside is " + arrCustomfeilds[i])
        contactuser = Contact.objects.create(
            datejoined = datejoined,
            notes = notes,
            emailaddress= emailaddress,
            firstname = firstname,
            lastname = lastname,
            jobtitle = jobtitle,
            company = company,
            mobilephone = mobilephone,
            workphone = workphone,
            country = country,
            stateprovince = stateprovince,
            city = city,
            address = address,
            zip = zip,
            website = website,
            addmethod = addmethod)
        contactuser.save()

        #make sure that username is unique for all who log in to the system
        objectQuerySettag = Contact.objects.filter(id = contactuser.id)
        #print(objectQuerySettag)
        dataB = serializers.serialize("json", objectQuerySettag, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=[
        'id',
        'status',
        'lifetimevalue', 
        'datejoined', 
        'notes',
        'emailaddress',
        'firstname',
        'lastname',
        'jobtitle',
        'company',
        'mobilephone',
        'workphone',
        'country',
        'stateprovince',
        'city',
        'address',
        'zip',
        'website',
        'stopmethod',
        'confirmquestionmark',
        'addmethod',
        'signupsource',
        'totalreviewsleft',
        'lastemailratingdone'
        ])
        #print(list(dataB))
        json_object = json.loads(dataB)
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        #return JsonResponse(response)
        return JsonResponse(json_object,safe=False)


    else:
        #arrCustomfeilds = request.GET.getlist('arrCustomfeilds')
        #print("arrcustomfeild is " + arrCustomfeilds)
        datejoined = request.GET['datejoined']
        notes = request.GET['notes']
        emailaddress= request.GET['emailaddress']
        firstname = request.GET['firstname']
        lastname = request.GET['lastname']
        jobtitle = request.GET['jobtitle']
        company = request.GET['company']
        mobilephone = request.GET['mobilephone']
        workphone = request.GET['workphone']
        country = request.GET['country']
        stateprovince = request.GET['stateprovince']
        city = request.GET['city']
        address = request.GET['address']
        zip = request.GET['zip']
        website = request.GET['website']
        addmethod = request.GET['addmethod']
    #firstname = request.GET['firstname']
    #lastname = request.GET['lastname']
    #arrCustomfeilds = request.GET.getlist('arrCustomfeilds')
    #for i in arrCustomfeilds:
    #    print("arrcustomfeild inside is " + i)

    #dataB=[firstname, lastname, arrCustomfeilds]
        dataB=[datejoined]
    #return JsonResponse(response)
        """
        contactuser = Contact.objects.create(
            datejoined = datejoined,
            notes = notes,
            emailaddress= emailaddress,
            firstname = firstname,
            lastname = lastname,
            jobtitle = jobtitle,
            company = company,
            mobilephone = mobilephone,
            workphone = workphone,
            country = country,
            stateprovince = stateprovince,
            city = city,
            address = address,
            zip = zip,
            website = website,
            addmethod = addmethod)
        contactuser.save()
        """
        
        return JsonResponse(dataB,safe=False)

            







def signout(request):
    auth.logout(request)
    messages.success(request, 'Logged Out Sucessfully!')
    return render(request, 'pages/signin.html')

def recoverpassword(request):

    if request.method == 'POST':
        user_email = request.POST['email']
        associated_user = User.objects.filter(email=user_email).first()
        if associated_user:
            current_site = get_current_site(request)
            email_subject = "Password Reset request"
            #the file which will hold the message being sent
            message2 = render_to_string('templateactivateaccount.html',{
            
            'name': associated_user.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
            'token': generate_token.make_token(associated_user)
            })
            email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [associated_user.email],
            )
            email.fail_silently = True

            if email.send():
                messages.success(request, " Password reset sent. We emailed you instructions for setting your password. If an account exist you should  receive them shortly.")

            else:
                messages.error(request, "Problems sending reset password email")

        return redirect('signin')
        #return redirect(request, 'signin')
            #email.fail_silently = True
            #email.send()


    return render(request, 'pages/recoverpassword.html')

def activate(request,uidb64,token):
    try:
        #the id is uid
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('index')
    else:
        return render(request,'activation_failed.html')


def reset(request, uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "You can change your password!!")
        return redirect('resetpasswordconfirm')
    else:
        return render(request,'activation_failed.html')


def resetpasswordconfirm(request):

    if request.method == "POST":
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        
        if password == cpassword:
            # Saving to DB using Django ORM - the best way
            current_user = request.user 
            current_user.password
            #h = (str)(current_user.id)
            myuser = User.objects.get(pk = (str)(current_user.id))
            #myuser = User.objects.get(pk=uid)

            #myuser.password = password
            # you want to set it this way because it keeps the hash of the password in the database
            myuser.set_password(password)
            #myuser.username = myuser.username
            myuser.save()
            #User.objects.create(password=password)
            #User.save()
            messages.success(request, "Your password has been set. You may go ahead and <b>log in </b> now.")
            return redirect('signin')
        else:
            messages.error(request, "The two passwords do not match")
            return redirect('resetpasswordconfirm')

    return render(request,'pages/resetpasswordconfirm.html')

    #if request.method == 'POST':
    #    return redirect('signin')
    """
    User = User
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':


            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been set. You may go ahead and <b>log in </b> now.")
                return redirect('signin')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = SetPasswordForm(user)
        return render(request, 'password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "Link is expired")

    messages.error(request, 'Something went wrong, redirecting back to Homepage')
    return redirect("signin")
    """


    return render(request,'pages/resetpasswordconfirm.html')



class CreateAccountInformationApis(generics.ListCreateAPIView):
    serializer_class = Staff3Serializer
    queryset = Staff.objects.all()

    def post(self, request, pk=None):
        
        firstname = request.data['firstname']
        lastname = request.data['lastname']
        username = request.data['username']
        id = request.data['id']
        
        holder = Staff.objects.get(id=id)
        #holder.userid
        User.objects.filter(id=holder.userid).update(first_name= firstname, last_name=lastname, username = username)
        Staff.objects.filter(id=id).update(firstname= firstname, lastname=lastname, username = username)

        #userstaff2 = Staff.objects.get(id = staffuser.id)

        #querysetsandcf = JoinStaffCustomfeild.objects.filter(staffid = userstaff).only('customfeildid__id','customfeildid__name','customfeildid__customfeildintvalue','customfeildid__customfeildstringvalue','customfeildid__dateofcreation','customfeildid__lastcustomfeildupdate')
       
   
        serializer2 = Staff3Serializer(holder,many=False)

        print("*******************")
        print(serializer2.data)
       
        return Response(serializer2.data)
    
        


def accountinformation(request):



    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        industry = request.POST['industry']
        

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('accountinformation')

        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('accountinformation')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('accountinformation')

        User.objects.filter(pk=request.user.id).update(username = username, first_name= fname, last_name=lname)
        Staff.objects.filter(userid=request.user.id).update(username = username, firstname= fname, lastname=lname, industry = industry)
        
        #myuser = User.objects.create_user(username, email)
        #myuser.first_name = fname
        #myuser.last_name = lname

        #this is whats stopping my loging in from working
        #for now we will leave it uncommented
        #myuser.is_active = False
        
        #myuser.save()
        #staffuser = Staff.objects.create(userid=myuser.id ,username=username, firstname=fname, lastname=lname, emailaddress=email, industry=industry)
        #staffuser.save()
        messages.success(request, "Your have updated your account information")
        return redirect('accountinformation')

        




    current_user = request.user 
    #i dont know why this aint commented out but imma do it now
    #Staff.objects.get()
    
    stafholderobjectQuerySet = Staff.objects.filter(userid = current_user.id).values_list('userid', 'username', 'firstname', 'lastname', 'emailaddress', 'industry')
    # dataC = serializers.serialize("json", stafholderobjectQuerySet, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['userid', 'username', 'firstname', 'lastname', 'emailaddress', 'industry'])
    #select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date")
    #authid is in studentaccount, student account is a saparate fourign key and so is authid
    #i don't have to serialize the data befor putting it as a context cus thats not the purpose of serialization
    print(list(stafholderobjectQuerySet))
    #print(dataC)
    print("*******************************************************************************************************************")
    #fro this situation i just want the list so il leave it here
    context = {'allData': list(stafholderobjectQuerySet)}
    #context = {'allData': dataC}

    return render(request,'pages/accountinformation.html', context)





def importsubscribers(request):

    if request.method == 'POST':

        """
        print("********************************************************")
        #mytag = Tag.objects.create(id = 3,name="hero", dateofcreation = datetime.date.today())
        mytag = Tag.objects.create(name="hero3", dateofcreation = datetime.date.today())
        #Cannot assign "1": "Attachedtag.tagid" must be a "Tag" instance.
        mytag.save()
        #mytag2 = Tag.objects.create(name="hero4", dateofcreation = datetime.date.today())
        #Cannot assign "1": "Attachedtag.tagid" must be a "Tag" instance.
        #mytag.save()
        print(mytag)
        myattachedtag = Attachedtag.objects.create(dateofattachement = datetime.date.today(), tagid = mytag)
        myattachedtag.save()
        print(myattachedtag)
        objectQuerySet = Attachedtag.objects.all().values('tagid').distinct()
        #print(myattachedtag.objects.all())
        print(objectQuerySet)
        print(Attachedtag.objects.all())
        print(Attachedtag.objects.all().values())
        #myattachedtag2 = Attachedtag.objects.create(tagid = mytag)
        #myattachedtag2.save()
        #print(myattachedtag2)
        #print(myattachedtag.objects.all())
        objectQuerySet = Attachedtag.objects.all().select_related("tagid")
        #objectQuerySet = Attachedtag.objects.filter(tagid = , delete_appointment_row = False, start_date__lte = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, datetime.datetime.now().time().hour, datetime.datetime.now().time().minute, datetime.datetime.now().time().second)).select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date")
        #the feild should only be the feild of thebouter object not the inner object for it to work
        dataB = serializers.serialize("json", objectQuerySet, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['dateofattachement','tagid'])
        print("*********")
        print(objectQuerySet)
        print(dataB)
        print("********************************************************")
        

        """
        """
        print("_________________________________________________________________________")
        #mytag = Tag.objects.create(id = 3,name="hero", dateofcreation = datetime.date.today())
        mygroup = Group.objects.create(name="hero", dateofcreation = datetime.date.today())
        #Cannot assign "1": "Attachedtag.tagid" must be a "Tag" instance.
        mygroup.save()
        #print(mytag)
        myattachedgroup = Attachedgroup.objects.create(dateofattachement = datetime.date.today(), groupid = mygroup)
        myattachedgroup.save()
        print(myattachedgroup)
        objectQuerySetgroup = Attachedgroup.objects.all().values('groupid').distinct()
        print(objectQuerySetgroup)
        print(Attachedtag.objects.all())
        print(Attachedtag.objects.all().values())
        objectQuerySetgroup = Attachedgroup.objects.all().select_related("groupid")
        #the feild should only be the feild of thebouter object not the inner object for it to work
        dataC = serializers.serialize("json", objectQuerySetgroup, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['dateofattachement','groupid'])

        print("___________")
        print(objectQuerySetgroup)
        print(dataC)
        print("_____________________________________________________")
        """

        """
        print("_________________________________________________________________________")
        #mytag = Tag.objects.create(id = 3,name="hero", dateofcreation = datetime.date.today())
        myform = Form.objects.create(name="hero", dateofcreation = datetime.date.today())
        #Cannot assign "1": "Attachedtag.tagid" must be a "Tag" instance.
        myform.save()
        #print(mytag)
        myattachedform = AttachedForm.objects.create(dateofattachement = datetime.date.today(), formid = myform)
        myattachedform.save()
        print(myattachedform)
        objectQuerySetform = AttachedForm.objects.all().values('formid').distinct()
        print(objectQuerySetform)
        print(AttachedForm.objects.all())
        print(AttachedForm.objects.all().values())
        objectQuerySetform = AttachedForm.objects.all().select_related("formid")
        #the feild should only be the feild of thebouter object not the inner object for it to work
        dataD = serializers.serialize("json", objectQuerySetform, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['dateofattachement','formid'])
        print("___________")
        print(objectQuerySetform)
        print(dataD)
        print("_____________________________________________________")
        """

        """
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        objectQuerySettag = Attachedtag.objects.filter(tagid__type = "Identification").select_related("tagid")
        print(objectQuerySettag)
        dataE = serializers.serialize("json", objectQuerySettag, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['dateofattachement','tagid'])
        print(dataE)
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        """
        """
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        objectQuerySettag = Attachedtag.objects.filter(tagid__type = "Purchase").select_related("tagid")
        print(objectQuerySettag)
        dataE = serializers.serialize("json", objectQuerySettag, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['dateofattachement','tagid'])
        print(dataE)
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        """


        industry = request.POST['industry']
        #filegiven = request.POST['filegiven']
        fileg = request.FILES.get("filegiven")
        
        #fileg_file = Bulkimport.objects.create(filename=fileg.name,file=fileg, status = industry)
        #file_path= fileg_file.file.path
        


        
        #the reason why i had error with the radio button is cus i named the check box thesame name as the radio button
        dot = request.POST['dot']
        #dot = request.POST.get('dot')
 
        
        #checkboxtable = request.POST['119']
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        #print(filegiven)
        print(fileg)
        print(industry)
        print(dot)


        striped_name = dot.strip()
        #striped_name.replace(" ", "")
        #s.replace(" ", "")        
        #print("name_of_student.strip() = : " + name_of_student.strip())
        print("striped name is: " + striped_name)
        #turned to a list of the first name and last name
        #this doesn't work
        #firstname_lastname = striped_name.split(r'\W') #r'[\s]'
        # this works but i must import re first
        name_value_list = re.split("\W+", striped_name)
        #r'[^\w]'
        print("going into first_lastname: ")
        for h in name_value_list:
            print("_]"+h+"[_")

        print("out of the loop")
        print("firstname_lastname is: " + name_value_list[0] + name_value_list[1])
        print(name_value_list)
        #print(checkboxtable)
        #filegiven = request.FILES['filegiven']
        

        """
        maxlength = len(name_value_list[0:-1])

        for i in range(len(name_value_list[0:-1])):
            if(name_value_list[0:-1][i] == 'dotlist'):
                g = i+1
                h = "true"
                while h == "true":
                    if g >= maxlength or (name_value_list[0:-1][g] == 'dotlist') or (name_value_list[0:-1][g] == 'dotform') or (name_value_list[0:-1][g] == 'dottag' or (name_value_list[0:-1][g] == 'dotidentificationtag') or (name_value_list[0:-1][g] == 'dotpurchasetag')):
                        h = "false"
                    else:
                        g = g +1
                        #id of attached dotlist
                        name_value_list[g]
                        print("id of attached dotlist=" + name_value_list[g])
                        i= i+1
            if(name_value_list[0:-1][i] == 'dotform'):
                g = i+1
                h = "true"
                while h == "true":
                    if g >= maxlength or (name_value_list[0:-1][g] == 'dotlist') or (name_value_list[0:-1][g] == 'dotform') or (name_value_list[0:-1][g] == 'dottag' or (name_value_list[0:-1][g] == 'dotidentificationtag') or (name_value_list[0:-1][g] == 'dotpurchasetag')):
                        h = "false"
                    else:
                        g = g +1
                        #id of attached dotlist
                        name_value_list[g]
                        print("id of attached dotform=" + name_value_list[g])
                        i= i+1
            if(name_value_list[0:-1][i] == 'dottag'):
                g = i+1
                h = "true"
                while h == "true":
                    if g >= maxlength or (name_value_list[0:-1][g] == 'dotlist') or (name_value_list[0:-1][g] == 'dotform') or (name_value_list[0:-1][g] == 'dottag' or (name_value_list[0:-1][g] == 'dotidentificationtag') or (name_value_list[0:-1][g] == 'dotpurchasetag')):
                        h = "false"
                    else:
                        g = g +1
                        #id of attached dotlist
                        name_value_list[g]
                        print("id of attached dottag=" + name_value_list[g])
                        i= i+1

            if(name_value_list[0:-1][i] == 'dotidentificationtag'):
                g = i+1
                h = "true"
                while h == "true":
                    if g >= maxlength or (name_value_list[0:-1][g] == 'dotlist') or (name_value_list[0:-1][g] == 'dotform') or (name_value_list[0:-1][g] == 'dottag' or (name_value_list[0:-1][g] == 'dotidentificationtag') or (name_value_list[0:-1][g] == 'dotpurchasetag')):
                        h = "false"
                    else:
                        g = g +1
                        #id of attached dotlist
                        name_value_list[g]
                        print("id of attached dotidentificationtag=" + name_value_list[g])
                        i= i+1
            if(name_value_list[0:-1][i] == 'dotpurchasetag'):
                g = i+1
                h = "true"
                while h == "true":
                    if g >= maxlength or (name_value_list[0:-1][g] == 'dotlist') or (name_value_list[0:-1][g] == 'dotform') or (name_value_list[0:-1][g] == 'dottag' or (name_value_list[0:-1][g] == 'dotidentificationtag') or (name_value_list[0:-1][g] == 'dotpurchasetag')):
                        h = "false"
                    else:
                        g = g +1
                        #id of attached dotlist
                        name_value_list[g]
                        print("id of attached dotpurchasetag=" + name_value_list[g])
                        i= i+1

        """


                #  Saving POST'ed file to storage
        #file = request.FILES['myfile']
        file_name = default_storage.save(fileg.name, fileg)
        print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        print(file_name)
        print(fileg.name)
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print(fileg)
        
        #  Reading file from storage
        filex = default_storage.open(file_name)
        #file_url = default_storage.url(file_name)
        #print(filex)
        #print(file_url)
        



        bulkimporthere = Bulkimport.objects.create(datetime = timezone.now(), status = industry, filename = fileg.name, file = filex)
        bulkimporthere.save()
        attachedall = AttachedAll.objects.create(dateofattachement = timezone.now())
        attachedall.bulkimportid = bulkimporthere
        #attachedall.save()




        



        #obj = Attachedgroup.objects.get(pk=)
        if (name_value_list[0] =='dotlist'):
            for n in name_value_list[1:-1]:
                print("the value of n is =" + n)
                obj = Attachedgroup.objects.get(pk=int(n))
                attachedall.attachedgroupid = obj
                attachedall.save()
                #attachedall
                #fileg_file = Bulkimport.objects.create(filename=filegiven, status = industry, attachedgroupid = int(n))
        if (name_value_list[0] =='dotform'):
            for n in name_value_list[1:-1]:
                print("the value of n is =" + n)
                obj = AttachedForm.objects.get(pk=int(n))
                attachedall.attachedformid = obj
                attachedall.save()
        if (name_value_list[0] =='dottag'):
            for n in name_value_list[1:-1]:
                print("the value of n is =" + n)
                obj = Attachedtag.objects.get(pk=int(n))
                attachedall.attachedtagid = obj
                attachedall.save()
        if (name_value_list[0] =='dotidentificationtag'):
            for n in name_value_list[1:-1]:
                print("the value of n is =" + n)
                obj = Attachedtag.objects.get(pk=int(n))
                attachedall.attachedtagid = obj
                attachedall.save()
        if (name_value_list[0] =='dotpurchasetag'):
            for n in name_value_list[1:-1]:
                print("the value of n is =" + n)
                obj = Attachedtag.objects.get(pk=int(n))
                attachedall.attachedtagid = obj
                attachedall.save()
        

        attachedall.save()

        bulkimporthere.id  

        """
        dot = request.POST['dot0']
        
        dotall = request.POST['dotall']
        dotlist = request.POST['dotlist']
        dotform = request.POST['dotform']
        dottag = request.POST['dottag']
        dotidentificationtag = request.POST['dotidentificationtag']
        dotpurchasetag = request.POST['dotpurchasetag']

        
        f = request.FILES['filegiven']
        with open('myapp/static/upload/'+f.name, 'wb+') as destination:  
            for chunk in f.chunks():  
                destination.write(chunk)  
        
        """
        context = {'bulkimportid': bulkimporthere.id }
        #context = {'allData': dataC}


        return redirect(request,'matchtotable')
    return render(request,'pages/importsubscribers.html')

def matchtotable(request):

    return render(request,'pages/matchtotable.html')




def table_load_up(request):

    #timezone.now()
    #print("********************************************************")
    #mytag = Tag.objects.create(id = 3,name="hero", dateofcreation = datetime.date.today())
    mytag = Tag.objects.create(name="tagP", dateofcreation = timezone.now(), type="Purchase")#Identification
    #Cannot assign "1": "Attachedtag.tagid" must be a "Tag" instance.
    mytag.save()
    mytag2 = Tag.objects.create(name="TagI", dateofcreation = timezone.now(), type="Identification")#
    #Cannot assign "1": "Attachedtag.tagid" must be a "Tag" instance.
    mytag2.save()
    #print(mytag)
    myattachedtagP = Attachedtag.objects.create(dateofattachement = timezone.now(), tagid = mytag)
    myattachedtagP.save()
    myattachedtagI = Attachedtag.objects.create(dateofattachement = timezone.now(), tagid = mytag2)
    myattachedtagI.save()
    #print(myattachedtag)
    objectQuerySet = Attachedtag.objects.all().values('tagid').distinct()
    #print(objectQuerySet)
    #print(Attachedtag.objects.all())
    #print(Attachedtag.objects.all().values())
    objectQuerySet = Attachedtag.objects.all().select_related("tagid")
    #the feild should only be the feild of thebouter object not the inner object for it to work
    dataB = serializers.serialize("json", objectQuerySet, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['dateofattachement','tagid'])

    #print("*********")
    #print(objectQuerySet)
    #print(dataB)
    #print("********************************************************")
    






    #print("_________________________________________________________________________")
    #mytag = Tag.objects.create(id = 3,name="hero", dateofcreation = datetime.date.today())
    mygroup = Group.objects.create(name="groupo", dateofcreation = timezone.now())
    #Cannot assign "1": "Attachedtag.tagid" must be a "Tag" instance.
    mygroup.save()
    #print(mytag)
    myattachedgroup = Attachedgroup.objects.create(dateofattachement = timezone.now(), groupid = mygroup)
    myattachedgroup.save()
    #print(myattachedgroup)
    objectQuerySetgroup = Attachedgroup.objects.all().values('groupid').distinct()
    #print(objectQuerySetgroup)
    #print(Attachedtag.objects.all())
    #print(Attachedtag.objects.all().values())
    objectQuerySetgroup = Attachedgroup.objects.all().select_related("groupid")
    #the feild should only be the feild of thebouter object not the inner object for it to work
    dataC = serializers.serialize("json", objectQuerySetgroup, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['dateofattachement','groupid'])

   # print("___________")
   # print(objectQuerySetgroup)
    #print(dataC)
    #print("_____________________________________________________")
    



    #print("_________________________________________________________________________")
    #mytag = Tag.objects.create(id = 3,name="hero", dateofcreation = datetime.date.today())
    myform = Form.objects.create(name="Formo", dateofcreation = timezone.now())
    #Cannot assign "1": "Attachedtag.tagid" must be a "Tag" instance.
    myform.save()
    #print(mytag)
    myattachedform = AttachedForm.objects.create(dateofattachement = timezone.now(), formid = myform)
    myattachedform.save()
    #print(myattachedform)
    objectQuerySetform = AttachedForm.objects.all().values('formid').distinct()
    #print(objectQuerySetform)
    #print(AttachedForm.objects.all())
    #print(AttachedForm.objects.all().values())
    objectQuerySetform = AttachedForm.objects.all().select_related("formid")
    #the feild should only be the feild of thebouter object not the inner object for it to work
    dataD = serializers.serialize("json", objectQuerySetform, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['dateofattachement','formid'])
    #print("___________")
    #print(objectQuerySetform)
    #print(dataD)
    #print("_____________________________________________________")



    
    #print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    objectQuerySettagi = Attachedtag.objects.filter(tagid__type = "Identification").select_related("tagid")
    #print(objectQuerySettag)
    dataE = serializers.serialize("json", objectQuerySettagi, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['dateofattachement','tagid'])
    #print(dataE)
    #print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    

    #print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    objectQuerySettagp = Attachedtag.objects.filter(tagid__type = "Purchase").select_related("tagid")
    #print(objectQuerySettag)
    dataF = serializers.serialize("json", objectQuerySettagp, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['dateofattachement','tagid'])
    #print(dataE)
    #print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")



    current_user = request.user

 

    datetime.date.today() # Returns 2018-01-15
    #datetime.date.today().time().hour  #datetime.date' object has no attribute 'hour',can't use this for time specifically like in now()
    datetime.datetime.now().time().hour 


    #print(objectQuerySet)
    print("*********************************************************")
    #objectQuerySet = Attachedtag.objects.filter(tagid = )
    #objectQuerySet = Attachedtag.objects.filter(tagid = , delete_appointment_row = False, start_date__lte = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, datetime.datetime.now().time().hour, datetime.datetime.now().time().minute, datetime.datetime.now().time().second)).select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date")
    
    #dataB = serializers.serialize("json", objectQuerySet, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['id', 'name'])
    
    #dataB = "hi"
    response = {
        'allData': dataB, #,
        'allDatatwo': dataC, #,
        'allDatathree': dataD,
        'allDatafour':dataE,
        'allDatafive':dataF,
    }
    return JsonResponse(response)
    #return render(request,'pages/importsubscribers.html', response)


#FOR SOME REASON THIS FUNCTION DOESNT GET RUNED
def importsubscribers_load_table(request):
    print("you are in importasubscribers_load_table)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))")
    #action_to_take = request.GET.get('actionToTake', None)

    action_to_take = request.GET.get('actionToTake', None)

    print(action_to_take)

    print("you are in importasubscribers_load_table)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))")
   
    print("_________________________________________________________________________")
    objectQuerySetgroup = Attachedgroup.objects.all().values('groupid').distinct()
    print(objectQuerySetgroup)
    print(Attachedtag.objects.all())
    print(Attachedtag.objects.all().values())
    objectQuerySetgroup = Attachedgroup.objects.all().select_related("groupid")
    #the feild should only be the feild of thebouter object not the inner object for it to work
    dataB = serializers.serialize("json", objectQuerySetgroup, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['dateofattachement','groupid'])

    print("___________")
    print(objectQuerySetgroup)
    print(dataB)
    print("_____________________________________________________")
    if action_to_take == "List":
        print("_________________________________________________________________________")
        objectQuerySetgroup = Attachedgroup.objects.all().values('groupid').distinct()
        print(objectQuerySetgroup)
        print(Attachedtag.objects.all())
        print(Attachedtag.objects.all().values())
        objectQuerySetgroup = Attachedgroup.objects.all().select_related("groupid")
        #the feild should only be the feild of thebouter object not the inner object for it to work
        dataB = serializers.serialize("json", objectQuerySetgroup, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['dateofattachement','groupid'])

        print("___________")
        print(objectQuerySetgroup)
        print(dataB)
        print("_____________________________________________________")
    elif action_to_take =="Form":
        print("_________________________________________________________________________")
        objectQuerySetform = AttachedForm.objects.all().values('formid').distinct()
        print(objectQuerySetform)
        print(AttachedForm.objects.all())
        print(AttachedForm.objects.all().values())
        objectQuerySetform = AttachedForm.objects.all().select_related("formid")
        #the feild should only be the feild of thebouter object not the inner object for it to work
        dataB = serializers.serialize("json", objectQuerySetform, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['dateofattachement','formid'])
        print("___________")
        print(objectQuerySetform)
        print(dataB)
        print("_____________________________________________________")
    elif action_to_take =="Alltag":
        print("********************************************************")
        objectQuerySet = Attachedtag.objects.all().values('tagid').distinct()
        print(objectQuerySet)
        print(Attachedtag.objects.all())
        print(Attachedtag.objects.all().values())
        objectQuerySet = Attachedtag.objects.all().select_related("tagid")
        #objectQuerySet = Attachedtag.objects.filter(tagid = , delete_appointment_row = False, start_date__lte = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, datetime.datetime.now().time().hour, datetime.datetime.now().time().minute, datetime.datetime.now().time().second)).select_related("student_id").prefetch_related('student_id__auth_id').order_by("-start_date")
        #the feild should only be the feild of thebouter object not the inner object for it to work
        dataB = serializers.serialize("json", objectQuerySet, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['dateofattachement','tagid'])
        print("*********")
        print(objectQuerySet)
        print(dataB)
        print("********************************************************")
    elif action_to_take =="Identification":
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        objectQuerySettag = Attachedtag.objects.filter(tagid__type = "Identification").select_related("tagid")
        print(objectQuerySettag)
        dataB = serializers.serialize("json", objectQuerySettag, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['dateofattachement','tagid'])
        print(dataB)
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    elif action_to_take =="Purchase":
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        objectQuerySettag = Attachedtag.objects.filter(tagid__type = "Purchase").select_related("tagid")
        print(objectQuerySettag)
        dataB = serializers.serialize("json", objectQuerySettag, use_natural_foreign_keys=True, use_natural_primary_keys=False, fields=['dateofattachement','tagid'])
        print(dataB)
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")


    response = {
        'allData': dataB
    }
    #This doesn't work
    #action_to_take2 = request.GET['actionToTake']
    #print("this is action_to_takeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee: " + action_to_take + "and action_to_take2 is " + action_to_take2)
    print("------------------------------------------Going to importsubsribers now")
    #print("*************************************************************************************************************************")
    print("you are out ")
    """
    response = {
    'redirectpageid': action_to_take
    }
    """
    return JsonResponse(response)