
from django.conf.urls import url
from django.urls import include, path

from . import views

app_name = 'users'

urlpatterns = [

    path('login-signup/', views.login_signup, name='login_signup'),



]
