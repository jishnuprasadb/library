from . import views
from django.urls import path

urlpatterns = [
    path('',views.load_addpage,name='load_addpage'),
    path('add_num',views.add_num,name='add_num')

]
