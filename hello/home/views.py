from django.shortcuts import render
from datetime import datetime
from home.models import Contacts
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable": "This is a variable sent"
    }
    return render(request, 'index.html', context)
def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")
def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phnumber = request.POST.get('phnumber')
        purpose = request.POST.get('purpose')
        contacts = Contacts(name=name, email=email,phnumber=phnumber,purpose=purpose,date=datetime.today())
        contacts.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contacts.html')
    # return HttpResponse("This is contacts page")
def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page")
