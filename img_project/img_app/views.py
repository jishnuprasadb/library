from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect

from img_app.models import StudentRegistration

# Create your views here.
def add_student(request):
    return render(request,'add_student.html')

def add_student_details(request):
    if request.method=='POST':
        sname=request.POST['student_name']
        ph=request.POST['ph_no']
        eml=request.POST['eml']
        adrs=request.POST['adrs']
        image=request.FILES.get('file')
        student=StudentRegistration(student_name=sname,
                               phone_number=ph,
                                email=eml,
                                address=adrs,image=image)
        student.save()
        print("hii")
        return redirect('show_students')

def show_students(request):
    students=StudentRegistration.objects.all()
    return render(request,'show_stud.html',{'student':students})

def editpage(request,pk):
    student=StudentRegistration.objects.get(id=pk) 
    return render(request,'edit.html',{'students':student})

def edit_student_details(request,pk):
    if request.method=='POST':
        students = StudentRegistration.objects.get(id=pk)
        students.student_name = request.POST.get('student_name')
        students.phone_number= request.POST.get('ph_no')
        students.email = request.POST.get('eml')
        students.address= request.POST.get('adrs')
        students.image= request.FILES.get('file')
        students.save()
        return redirect('show_students')
    return render(request, 'edit.html',)

def delete_student(request,pk):
    students=StudentRegistration.objects.get(id=pk)
    students.delete()
    return redirect('show_students')
    