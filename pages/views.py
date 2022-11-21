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
#from pages import settings

# Create your views here.
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
        #myuser.is_active = False
        myuser.save()

        messages.success(request, "Your Account has been successfully created.")
        
        # Welcome Email
        subject = "Welcome to Mail Pinyata Login!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to Mail Pinyata!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\n"        
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

def signout(request):
    auth.logout(request)
    messages.success(request, 'Logged Out Sucessfully!')
    return render(request, 'pages/signin.html')

def recoverpassword(request):
    return render(request, 'pages/recoverpassword.html')

def activate(request,uidb64,token):
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
        messages.success(request, "Your Account has been activated!!")
        return redirect('index')
    else:
        return render(request,'activation_failed.html')