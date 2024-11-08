from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterUserForm
from .models import BlackList
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from .recaptcha import check_recaptcha
from .decorator import user_is_loggedin




#---------------$ register function $---------------#
#> if user already logged in can't go to this page <#
@user_is_loggedin()
def register_func(req):
    register_message = ''
    recaptcha_message = ''
    form = RegisterUserForm()
    if req.method == 'POST':
        user_email = req.POST.get('email')
        #- check if email in black list -#
        is_forbiden = BlackList.is_in_blacklist(useremail=user_email)
        if is_forbiden:
            #- send blocked username to HTML page -#
            req.session['blockedUser'] = user_email
            return redirect('forbidden_page')
        else:
            exist_email = User.objects.filter(email=user_email).exists()
            if not exist_email:
                form = RegisterUserForm(req.POST)
                if form .is_valid():
                    #- checke recaptcha -#
                    if check_recaptcha(req):
                        form.save()
                        return redirect('login_page')
                    else:
                        recaptcha_message = 'Invalid Recaptcha!'
            else:
                register_message = 'This Email Already Used!'

    ctx = {
        'registerForm':form,
        'register_message':register_message,
        'recaptcha_message':recaptcha_message
    }
    return render(req, 'sign_temps/register.html', ctx)



#---------------$ login function $---------------#
#> if user already logged in can't go to this page <#
@user_is_loggedin()
def login_func(req):
    message = ''
    recaptcha_message = ''
    if req.method =='POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        exist_user = authenticate(req, username=username, password=password)

        if exist_user:
            #- check if user forbidden -#
            is_forbidden= BlackList.is_in_blacklist(useremail=exist_user.email)
            if is_forbidden:
                #- send blocked username to HTML page -#
                req.session['blockedUser'] = exist_user.email
                return redirect('forbidden_page')
            else:
                #- checke recaptcha -#
                if check_recaptcha(req):
                    
                    login(req,exist_user)
                    return redirect('home_page')
                else:
                    recaptcha_message = 'Invalid Recaptcha!'
        else:
            message = 'Username Or Password Wrong!'
        
    ctx = {
        'message':message,
        'recaptcha_message':recaptcha_message
    }
    return render(req, 'sign_temps/login.html', ctx)



#---------------$ social login check blacklist $---------------#
'''
check if logged in SocialAccount in blacklist
or already its email used by anther user.
'''
def sociallogin_check(req):
    is_forbidden = BlackList.is_in_blacklist(useremail=req.user.email)
    if is_forbidden:
        logout(req)
        return redirect('forbidden_page')
    else:
        return redirect('home_page')


#---------------$ social login check if email already exists when sign up $---------------#
'''
this function go to
allauth accounts/3rdparty/signup/ who is the standrd signup page for allauth
but we link it the url with this function to
redirect to our built login page and show error message
when email used by another user
or another account (to unshow standard signup page and its options)
'''
def sociallogin_signup(req):
    messages.error(req, 'This Email Used By Anoter User! Try Again', extra_tags='social_error')
    return redirect('login_page')



#---------------$ logout function $---------------#
def logout_func(req):
    logout(req)
    return redirect('login_page')
