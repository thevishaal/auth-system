from django.shortcuts import render

# Create your views here.
def seller_dashboard(request):
    return render(request, "seller/dashboard.html")