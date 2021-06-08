from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages , auth


# Create your views here.
def login(request):

    if request.method == 'POST':
        print('--------login-------------')
        username = request.POST['username']
        password = request.POST['password']    

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request,   'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        # return render(request, 'accounts/login.html')
        return render(request, 'pages/CompanyLogin.html')

def register(request):
    if request.method == 'POST':
        # Get form values
        c_name = request.POST['c_name']
        address = request.POST['address']
        city = request.POST[' city ']
        state = request.POST['state']
        pin_code = request.POST['pin_code']
        email = request.POST['email']
        cp_name  = request.POST['cp_name']
        c_website  = request.POST['c_website']
        contact_no  = request.POST['contact_no']
        password = request.POST['password']
       
  
        # if username:   
        #     company = Company.objects.create_user(username=username, password=password, email=email,first_name=first_name,last_name=last_name)
        
        #     user.save()
            
    #         return redirect('login')
    #     else:
    #         messages.error(request,'Passwords do not match')
    #         return redirect('register')
    # else:
    #     return render(request, 'accounts/register.html')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']    

#         user = auth.authenticate(username=username,password=password)

#         if user is not None:
#             auth.login(request, user)
#             messages.success(request,   'You are now logged in')
#             return redirect('dashboard')
#         else:
#             messages.error(request, 'Invalid credentials')
#             return redirect('login')
#     else:
#         # return render(request, 'accounts/login.html')
#     return render(request, 'pages/CompanyRegister.html')

def myaccount(request):
    return render(request, 'pages/CompanyMyAccount.html')

def addnewjob(request):
    return render(request, 'pages/AddNewJob.html')

def viewpostedjob(request):
    return render(request, 'pages/ViewJob.html')

def logout(request):
    return render(request, 'pages/index.html')