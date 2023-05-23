import imp
from django.urls import path
from college_app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.home,name='home'),
    path('login_page',views.login_page,name='login_page'),
    path('signup_page',views.signup_page,name='signup_page'),
    path('usercreate',views.usercreate,name='usercreate'),
    path('teacher_login',views.teacher_login,name='teacher_login'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('view_profile',views.view_profile,name='view_profile'),
    path('add_course_page',views.add_course_page,name='add_course_page'),
    path('add_course',views.add_course,name='add_course'),
    path('add_student_page',views.add_student_page,name='add_student_page'),
    path('add_student',views.add_student,name='add_student'),
    path('show_student',views.show_student,name='show_student'),
    path('teacher_home',views.teacher_home,name='teacher_home'),
    
    path('edit_profile_page',views.edit_profile_page,name='edit_profile_page'),
    path('edit',views.edit,name='edit'),
    
    
    path('show_teacher',views.show_teacher,name='show_teacher'),
    path('delete_student/<int:pk>',views.delete_student,name='delete_student'),
    path('delete_teacher/<int:pk>',views.delete_teacher,name='delete_teacher'),
    path('logout',views.logout,name='logout')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)