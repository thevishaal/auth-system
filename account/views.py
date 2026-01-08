from django.shortcuts import render, redirect
from account.forms import RegistrationForm
from django.contrib import messages

# Create your views here.
def login_view(request):
    return render(request, "account/login.html")


def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.is_active = False
            user.save()
            messages.success(request, "Registration successful! Please check your email to actovate your accoutn.")
            return redirect('account:login_view')
    else:
        form = RegistrationForm()
    return render(request, "account/register.html", {'form': form,})