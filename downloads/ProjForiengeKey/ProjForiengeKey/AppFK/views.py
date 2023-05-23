from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def Home(request):
    return render(request,'home.html')


def CoursePage(request):
    return render(request,'addcourse.html')


def AddCourse(request):
    if request.method == 'POST':
        coursename=request.POST['coursename']
        coursefees=request.POST['coursefees']
        data = CourseModel(Course_Name=coursename,Course_Fees=coursefees)
        data.save()
        # messages.info(request, 'New User Added')
        return redirect('Home')


def StudentPage(request):
    courses=CourseModel.objects.all()
    context={'courses':courses}
    return render(request,'addstudent.html',context)


def AddStudent(request):
    if request.method=='POST':
        stdname=request.POST['stdname']
        stdaddress=request.POST['stdaddress']
        stdage=request.POST['stdage']
        # joindate=request.POST['joindate']
        select=request.POST['select']
        course=CourseModel.objects.get(id=select)
        data = StudentModel(Std_Name=stdname,Std_Address=stdaddress,Std_Age=stdage,Course=course)
        data.save()
        return redirect('Home')


def StudentDetails(request):
    student_detail = StudentModel.objects.all()
    return render(request,'studentdetail.html',{'student':student_detail})


def Tables(request):
        course=CourseModel.objects.all()
        student=StudentModel.objects.all()
        return render(request,'table.html',{'cdata':course,'sdata':student})