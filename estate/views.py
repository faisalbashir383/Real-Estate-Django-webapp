from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Property,Contact,Service,Testmonial


def index(request):
    testmonial = Testmonial.objects.all()
    context = {'testmonial':testmonial}
    return render(request,'index.html')
def about(request):
   return render(request,'about.html')
def services(request):
    service = Service.objects.all()
    context = {'service':service}    
    return render(request,'services.html',context) 
def property(request):
    property = Property.objects.all()
    context = {'property':property}
    return render(request,'property.html',context)
def work(request):
   return render(request,'work.html')
def team(request):
   return render(request,'team.html')
def contact(request):
    return render(request,'contact.html')   
  
    
    
    
    
