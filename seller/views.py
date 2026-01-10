from django.shortcuts import render, redirect
from core.decorators import login_and_role_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
@login_and_role_required("seller")
def seller_dashboard(request):
    return render(request, "seller/dashboard.html")


@login_and_role_required("seller")
def password_change_view(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            logout(request)
            messages.success(request, "Password changed successfully. Please log in with your new password.")
            return redirect("account:login_view")
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request, "seller/password_change.html")