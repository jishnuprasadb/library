from django.contrib import admin

# Register your models here.
from django.contrib import admin
from admin_app.models import CourseModel,StudentModel
# Register your models here.


@admin.register(CourseModel)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display=('id','Course_Name','Course_Fees')

@admin.register(StudentModel)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display=('id','Course','Std_Name','Std_Address','Std_Age','Join_Date')
    
