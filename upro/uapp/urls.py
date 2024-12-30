from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.login_user,name='login'),
   path('signin',views.signup,name='signin'),
   path('welcome',views.main,name='main'),
   path('logout',views.logout_g,name='logout')
    
]
