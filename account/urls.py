from django.urls import path
from account.views import login_view, register_view


app_name = 'account'
urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),   
]