from django.shortcuts import render

# Create your views here.
def load_first_page(request):
    return render(request,'first_page.html')
     
def load_second_page(request):
    return render(request,'second_page.html')     