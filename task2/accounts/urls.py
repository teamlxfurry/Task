from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
   path('',index, name='index'),
   path("login",login,name="login"),
   path("register",register,name="register"),
   path("success",success,name="success"),
   path("token",token,name="token"),
   path("verify/auth_token",verify,name="verify"),
   path("error",error,name='error'),
   ]