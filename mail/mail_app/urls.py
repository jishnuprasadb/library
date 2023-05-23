from unicodedata import name
from django.urls import path,include

from mail_app.views import stdform

urlpatterns = [
    path('',stdform,name='stdform')
]
