from django.urls import path
from customer.views import customer_dashboard

app_name = 'customer'
urlpatterns = [
    path('dashboard', customer_dashboard, name='customer_dashboard'),
]