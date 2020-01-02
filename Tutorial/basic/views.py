from django.shortcuts import render
from django.http import HttpResponse
from . models import Contact
from django.template import loader
# Create your views here.

def home(request):
    return HttpResponse("You are at home.Thanks :)")

def detail(request, contact_id):
    parameter=Contact.objects.get(pk=contact_id)
    context={
        'parameter':parameter
    }
    return render(request,'basic/detail.html',context)

def all(request):
    parameter=Contact.objects.all()
    context={
        'parameter':parameter
    }
    return render(request,'basic/all.html',context)

def delete(request,contact_id):
    parameter=Contact.objects.get(pk=contact_id)
    parameter.delete()
    return all(request)

def add(request):
    return render(request,'basic/add.html')

def insert(request):
    name=request.POST['contact_name']
    number=request.POST['contact_number']
    email=request.POST['contact_email']
    C1=Contact(contact_name=name,contact_number=number,contact_email=email)
    C1.save()
    return all(request)

def fill(request,contact_id):
    parameter=Contact.objects.get(pk=contact_id)
    context={
        'parameter':parameter
    }
    return render(request,'basic/fill.html',context)
    
def update(request,contact_id):
    
    name=request.POST['contact_name']
    number=request.POST['contact_number']
    email=request.POST['contact_email']
    C1=Contact.objects.get(pk=contact_id)
    C1.contact_name=name
    C1.contact_number=number
    C1.contact_email=email
    C1.save()
    return all(request)
    
    