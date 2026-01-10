from django.shortcuts import render, redirect
from account.forms import RegistrationForm
from account.models import User
from django.contrib import messages
from django.conf import settings
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from account.utils import send_activation_email
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_seller:
            return redirect('seller:seller_dashboard')
        elif request.user.is_customer:
            return redirect('customer:customer_dashboard')
        return redirect('core:home')
    
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if not email or not password:
            messages.error(request, "Both Fields are required!")
            return redirect("account:login_view")
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password")
            return redirect("account:login_view")
        
        if not user.is_active:
            messages.error(request, "Your account is inactive. Please activate your account.")
            return redirect("account:login_view")
        
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)

            if request.user.is_seller:
                return redirect('seller:seller_dashboard')
            elif request.user.is_customer:
                return redirect('customer:customer_dashboard')
            else:
                messages.error(request, "You do not have permission to access this area.")
                return redirect("core:home")
        else:
            messages.error(request, "Invalid email or password")
            return redirect("account:login_view")

    return render(request, "account/login.html")


def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.is_active = False
        
            role = request.POST.get('role')
            if role ==  "seller":
                user.is_seller = True
                user.is_customer = False
            elif role ==  "customer":
                user.is_seller = False
                user.is_customer = True

            user.save()
            
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = reverse("account:activate", kwargs={'uidb64': uidb64, 'token': token})
            activation_url = f"{settings.SITE_DOMAIN}{activation_link}"
            send_activation_email(user.email, activation_url)

            messages.success(request, "Registration successful! Please check your email to activate your account.")
            return redirect('account:login_view')
    else:
        form = RegistrationForm()
    return render(request, "account/register.html", {'form': form,})


def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        if user.is_active:
            messages.warning(request, "This account has already been activated.")
            return redirect("account:login_view")
        
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Your account has been activated successfully!")
            return redirect("account:login_view")
        else:
            messages.error(request, "The activation link is invalid or has expired.")
            return redirect("account:login_view")

    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        messages.error(request, "Invalid activation link.")
        return redirect("account:login_view")