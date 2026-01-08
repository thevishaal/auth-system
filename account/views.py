from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, "account/login.html")


def signup(request):
    return render(request, "account/register.html")