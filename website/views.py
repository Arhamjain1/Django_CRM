from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm

# request is going to that webpage and requesting that webpage
def home(request):
    #Check to see if logging in

    if request.method=='POST': #This checks if the HTTP request method is POST. Typically, a POST request is used for form submissions (like logging in).
        username=request.POST['username'] #Whataver user mentiones in the username field in form it will be stored in the variable username
        password=request.POST['password'] #Same above like of username for password
        #Authenicate checks credentials provided returning usr object if correct else None
        user=authenticate(request,username=username,password=password)

        if user is not None:

#If authenticate returns a valid user (user is not None), the login function logs the user in by attaching the user object to the session.
#messages.success is used to set a success message to be displayed to the user.

            login(request,user)
            messages.success(request,"You have been logged in")
            return redirect('home') #Where we have authentication true 
    
        else: #Handleing None condition
            messages.success(request,"There was an error logging in please try again....") #else part in home html where we have the same webpag with error thrown above.
            return redirect('home')
    else: #Handle GET Condition
        return render(request,'home.html',{})
    

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out !")
    return render(request,'home.html',{})

def register_user(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password='password')
            login(request,user)
            messages.success(request,"You have succesfully registered.")
            return redirect('home')
    else:
        form=SignUpForm()    
    return render(request,'register.html',{'form':form})