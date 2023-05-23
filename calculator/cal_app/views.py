from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def calculate(request):
    c=''
    n1=int(request.POST.get('number1'))
    n2=int(request.POST.get('number2'))
    if request.method=='POST':
        if 'opr'=='+':
            c=n1+n2
        elif 'opr'=='-':
            c=n1-n1
        elif 'opr'=='*':
            c=n1*n2
        elif 'opr'=='/':
            c=n1/n2
    return render(request,'home.html',{'result':c})                    

