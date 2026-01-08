from django.urls import path
from account.views import login_view, signup


app_name = 'account'
urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('signup/', signup, name='signup'),   
]