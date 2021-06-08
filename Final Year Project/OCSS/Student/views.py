from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
    
def slogin(request):
    return render(request, 'pages/StudentLogin.html')

def sregister(request):
    return render(request, 'pages/StudentRegister.html')

def smyaccount(request):
    return render(request, 'pages/StudentMyAccount.html')

def jobmatches(request):
    return render(request, 'pages/JobMatches.html')

def appliedjob(request):
    return render(request, 'pages/AppliedJob.html')

def slogout(request):
    return render(request, 'pages/index.html')    
