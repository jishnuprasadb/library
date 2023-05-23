from django.shortcuts import render

# Create your views here.
def load_addpage(request):
    return render(request,'add.html')

def add_num(request):
    n1=int(request.GET.get('number1'))
    n2=int(request.GET.get('number2'))
    sum=n1+n2
    return render(request,'result.html',{'result':sum})