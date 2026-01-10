from django.urls import path
from seller.views import seller_dashboard, password_change_view


app_name = 'seller'
urlpatterns = [
    path('seller/dashboard/', seller_dashboard, name='seller_dashboard'),
    path('change-password/', password_change_view, name='password_change_view'),
]