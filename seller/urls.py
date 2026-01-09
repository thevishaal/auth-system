from django.urls import path
from seller.views import seller_dashboard


app_name = 'seller'
urlpatterns = [
    path('seller/dashboard/', seller_dashboard, name='seller_dashboard'),
]