from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
  path('',views.index,name="index"),
  # path('about/',views.about,name="about")
  path('deletion/<int:id>',views.delete_g,name='deletion'),
   path('edit_g/<int:id>',views.edit_g,name='edit_g'),
  
]