from django.shortcuts import render, HttpResponse, redirect
# now we'll be importing home models to store the
# data in the contact model
from home.models import Contact
# for using message for alerting
from django.contrib import messages
#important we are using "auth.models" since a model "User"
#is already created in django admin which will handle user
#signup and we explicitly dont have to make a model for user
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    return render(request, "home/home.html")


def about(request):
    return HttpResponse('this is about')


def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        # make an object of Contact model
        if len(name) < 2:
            messages.error(request, 'your form has not been submitted')
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            # we also need to save it to as to reflect in django admin
            contact.save()
            messages.success(request, 'your issue has been submitted!')

    return render(request, 'home/contact.html')

# now makind vewis for signup page


def handleSignup(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

    #checking user inputs valid credentials
        if len(username)>10:
            messages.error
        
    # creating users
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'your account have been successfully created!')
        
        return redirect("home")

    else:
        return HttpResponse("error 404 not found")

#handling login and logout

def handleLogin(request):
    if request.method =='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpass']

        user = authenticate(username = loginusername, password = loginpassword)
        # the above line will retun none if the user is not found
        # therfore:

        if user is not None:
            login(request, user)
            messages.success(request, "welcome aboard!")
            return redirect("home")
        else:
            messages.error(request, "Sorry invalid credentials, try again!")
            return redirect('home')

def handleLogout(request):
    logout(request)
    messages.warning(request, "session logged out!")
    return redirect("/")
    

