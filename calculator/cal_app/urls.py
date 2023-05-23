from . import views
from django.urls import path

urlpatterns=[
    path('',views.home,name='home'),
    path('calculate',views.calculate,name='calculate')
]