
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from college_app.models import Course,Student,Teacher
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,'home.html')

def login_page(request):
    return render(request,'login_page.html')    

def signup_page(request):
    courses=Course.objects.all()
    context={'course':courses}
    return render(request,'signup.html',context)    

def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']
        if password==cpassword: 
            if User.objects.filter(username=username).exists(): 
                messages.info(request, 'This username already exists!!!!!!')
                return redirect('signup_page')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                select=request.POST['select']
                course=Course.objects.get(id=select)
                phone_number=request.POST['ph_no']
                age=request.POST['age']
                image=request.FILES.get('file')
                address=request.POST['adrs']
                data=User.objects.get(id=user.id)
                user=Teacher(user=data,course=course,phone_number=phone_number,age=age,photo=image,address=address)
                user.save()
                print("Successed...")
                return redirect('login_page')
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signup_page')   
        
    
def teacher_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('admin_home')
            else:
                login(request,user)
                auth.login(request,user) 
                return redirect('teacher_home')   
        
        
@login_required(login_url='login_page')
def admin_home(request):
    return render(request,'admin_home.html')

@login_required(login_url='login_page')
def teacher_home(request):
    return render(request,'teacher_home.html')


@login_required(login_url='teacher_login')
def view_profile(request):
    teacher=Teacher.objects.get(user=request.user)  
    return render(request,'view_profile.html',{'teacher':teacher})    


@login_required(login_url='teacher_login')
def add_course_page(request):
    return render(request,'add_course.html')

@login_required(login_url='teacher_login')
def add_student_page(request):
    courses=Course.objects.all()
    context={'course':courses}
    return render(request,'add_student.html',context)

def add_course(request):
    if request.method=='POST':
        course_name=request.POST['course_name']
        course_fee=request.POST['course_fee']
        course=Course(Course_Name=course_name,Course_Fee=course_fee)
        course.save()
        print('hii')
        return redirect('admin_home')

def add_student(request):
    if request.method=='POST':
        name=request.POST['student_name']
        age=request.POST['age']
        email=request.POST['email']
        ph_no=request.POST['ph_no']
        select=request.POST['select']
        course=Course.objects.get(id=select)
        student=Student( course=course,std_name=name, std_age=age,email=email, phone_number=ph_no,)
        student.save()
        print('hii')
        return redirect('admin_home')

@login_required(login_url='teacher_login')
def show_student(request):
    student=Student.objects.all()
    return render(request,'show_student.html',{'student':student})        

@login_required(login_url='teacher_login')
def edit_profile_page(request):
    teacher=Teacher.objects.get(user=request.user)
    course=Course.objects.all()
    return render(request,'editpage.html',{'teacher':teacher,'course':course})

def edit(request):
    if request.method=='POST':
        teacher=Teacher.objects.get(user=request.user)
        teacher.user.first_name=request.POST.get('first_name')
        teacher.user.last_name=request.POST.get('last_name')
        teacher.user.email=request.POST.get('email')
        teacher.course.Course_Name=request.POST.get('select')
        teacher.phone_number=request.POST.get('ph_no')
        teacher.age=request.POST.get('age')
        teacher.photo=request.FILES.get('file')
        teacher.address=request.POST.get('adrs')
        teacher.save()
        return redirect('teacher_home')

@login_required(login_url='teacher_login')
def show_teacher(requst):
    teacher=Teacher.objects.all()  
    return render(requst,'show_teacher.html',{'teacher':teacher})     

def delete_student(request,pk):
    student=Student.objects.get(id=pk)
    student.delete()
    return redirect('show_student')

def delete_teacher(request,pk):
    teacher=Teacher.objects.get(id=pk)
    teacher.delete()    
    return redirect('show_techer')
    
login_required(login_url='teacher_login')
def logout(request):
	auth.logout(request)
	return redirect('home')    