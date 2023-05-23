from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def kozhikode(request):
    return render(request,'kozhikode.html')    

def thrissur(request):
    return render(request,'thrissur.html')

def eranakulam(request):
    return render(request,'eranakulam.html')

def alappuzha(request):
    return render(request,'alappuzha.html')             