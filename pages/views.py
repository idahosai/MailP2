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
