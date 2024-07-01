from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record
# request is going to that webpage and requesting that webpage
def home(request):
    #grab everything in the table and assign in record
    records=Record.objects.all() #Its Like SELECT * FROM Record;.


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
        return render(request,'home.html',{'records':records})
    #In above line records is the name of the variable accessible in home html.The value (records) is the data you want to pass to the template.
    

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out !")
    return render(request,'home.html',{})

def register_user(request):
    if request.method=='POST':   #When a form is submitted, the method is POST. If this condition is true, it means the user has submitted the registration form.
        form=SignUpForm(request.POST) #an instance of SignUpForm with the data submitted in the form (request.POST). request.POST is a dictionary-like object containing all the data submitted via the form.
        if form.is_valid():
            form.save()
            #Authenticate and login

            #form.cleaned_data is a dictionary containing the validated and cleaned data from the form. This line retrieves the username and password from the cleaned data.
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            #If they do authenticate, it returns a User object; otherwise, it returns None.
            user=authenticate(username=username,password=password)
            
            #If authentication is successful, this logs the user in by creating a session for them. The login function takes the current request and the authenticated user as parameters.
            login(request,user)
            messages.success(request,"You have succesfully registered.")
            return redirect('home')
    else:
        #If the request method is not POST (e.g., if the user just visited the registration page), this creates a new, empty instance of SignUpForm. This means no data is pre-filled in the form.
        form=SignUpForm()    
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        #LookUp Records
        customer_record=Record.objects.get(id=pk) #Get id primary key form the models.py defined
        return render(request,'record.html',{'customer_record':customer_record})
    else:
        messages.success(request,"You must be logged in !")
        return redirect('home')
    
def delete_customer(request,pk):
    if request.user.is_authenticated:
        delete_it=Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Record Deleted Successfully....")
        return redirect('home')
    else:
        messages.success(request,"You must be logged in....")
        return redirect('home')

def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(request,"Record Added")
                return redirect('home')
            
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,"You Must be Logged In......")
        return redirect('home')
#render processes a template and returns an HTML response for the current request, keeping the user on the same URL.
#redirect instructs the browser to make a new request to a different URL, changing the URL in the browser's address bar.




#AddRecordForm: The form class used for creating or updating records.
#request.POST or None: This passes the POST data if the form is submitted, or None if it’s just a GET request to initially load the form.
#instance=current_record: Binds the form to the current_record instance so that the form is pre-populated with the current data of the record.
def update_record(request,pk):
    if request.user.is_authenticated:
        current_record=Record.objects.get(id=pk)
        form=AddRecordForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record has been updated")
            return redirect('home')
        return render(request,'update_record.html',{'form':form})
    else:
        messages.success(request,"You must be logged in...")
        return redirect('home')