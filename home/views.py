from django.shortcuts import render, HttpResponse
#now we'll be importing home models to store the
#data in the contact model
from home.models import Contact
#for using message for alerting
from django.contrib import messages

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
        #make an object of Contact model
        if len(name)<2:
            messages.error(request, 'your form has not been submitted')
        else:
            contact = Contact(name = name, email = email, phone= phone, content = content)
            #we also need to save it to as to reflect in django admin
            contact.save()
            messages.success(request, 'your issue has been submitted!')
    
    return render(request, 'home/contact.html')
