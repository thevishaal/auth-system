from django.urls import path
from customer.views import customer_dashboard, password_change_view

app_name = 'customer'
urlpatterns = [
    path('dashboard/', customer_dashboard, name='customer_dashboard'),
    path('password-change/', password_change_view, name='password_change_view'),
]