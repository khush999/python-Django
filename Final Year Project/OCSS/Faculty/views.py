from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def flogin(request):
    return render(request, 'pages/FacultyLogin.html')

def fregister(request):
    return render(request, 'pages/FacultyRegister.html')

def reviewstudent(request):
    return render(request, 'pages/ReviewStudent.html')

def flogout(request):
    return render(request, 'pages/index.html')