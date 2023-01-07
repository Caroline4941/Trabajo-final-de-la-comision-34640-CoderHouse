from django.urls import path
from login.views import *

urlpatterns = [
    path("accounts/login/", login_request, name="login"),
    path("", login_request, name="login"),

]