from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Account
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.urls import reverse


# Activatetion Account
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode , urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages




def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']    # @gmail.com
            country = form.cleaned_data['country']
            password = form.cleaned_data['password']
            user_name = email.split('@')[0] # django123
            phone_number = form.cleaned_data['phone_number']

            user = Account.objects.create_user(first_name=first_name, last_name=last_name,email=email, country=country, username=user_name, password=password)

            user.phone_number = phone_number

            user.save()

            # User Activate
            doman_name = get_current_site(request) 
            mail_subject = 'Please activate your account'
            message = render_to_string('accounts/account_verification_email.html', {
                'user':user,
                'domain':doman_name,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)), 
                'token':default_token_generator.make_token(user),
            })

            to_email = email
            send_mail = EmailMessage(mail_subject, message,to=[to_email])
            send_mail.send()
            return redirect(reverse('accounts:login') + f'?command=verification&email={email}')
    else:
        form = RegisterForm()    

    context = {
        'form':form,
    }     

    return render(request, 'accounts/register.html', context)



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                messages.success(request, 'Login is successful.')
                # return redirect('store:home')
            else:
                messages.error(request, 'Your account is inactive.')
        else:
            messages.error(request, 'Invalid login credentials.')

        return redirect('accounts:login')

    return render(request, 'accounts/login.html')




def activate(reqeust, uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
            user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(reqeust, 'Your Account Is Activated.')
        return redirect('accounts:login')
    else:
        messages.error(reqeust, 'Your Account is not active, please try again.')
        return redirect('accounts:register')