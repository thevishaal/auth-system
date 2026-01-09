from django.shortcuts import render
from core.decorators import login_and_role_required

# Create your views here.
@login_and_role_required("seller")
def seller_dashboard(request):
    return render(request, "seller/dashboard.html")