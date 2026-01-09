from django.urls import path
from account.views import login_view, register_view, activate_account
from django.contrib.auth.views import LogoutView


app_name = 'account'
urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),  
    path('activate/<str:uidb64>/<str:token>/', activate_account, name='activate'), 
    path('logout/', LogoutView.as_view(), name='logout'),
]