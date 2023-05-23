from django.urls import path
from admin_app import views
from django.contrib import admin

# from AppEmail.views import stdform

urlpatterns = [
    path("",views.Home,name="Home"),
    path("CoursePage",views.CoursePage,name="CoursePage"),
    path("StudentPage",views.StudentPage,name="StudentPage"),
    path("AddCourse",views.AddCourse,name="AddCourse"),
    path("AddStudent",views.AddStudent,name="AddStudent"),
    path("StudentDetails",views.StudentDetails,name="StudentDetails"),
    path('Tables',views.Tables,name='Tables')
    

]