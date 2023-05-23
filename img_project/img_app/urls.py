from img_app import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.add_student,name='add_student'),
    path('add_student_details',views.add_student_details,name='add_student_details'),  # type: ignore
    path('show_students',views.show_students,name='show_students'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('edit_student_details/<int:pk>',views.edit_student_details,name='edit_student_details'),
    path('delete_student/<int:pk>',views.delete_student,name='delete_student')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)