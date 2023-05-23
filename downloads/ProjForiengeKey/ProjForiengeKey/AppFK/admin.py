from django.contrib import admin
from AppFK.models import CourseModel,StudentModel
# Register your models here.


@admin.register(CourseModel)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display=('id','Course_Name','Course_Fees')

@admin.register(StudentModel)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display=('id','Course','Std_Name','Std_Address','Std_Age','Join_Date')
    
