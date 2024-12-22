from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'website\index.html') 

def about(request):
    return render(request, 'website\\about.html')

def contact(request):
    return render(request, 'website\contact.html')

def counselor(request):
    return render(request, 'website\counselor.html')

def pricing(request):
    return render(request, 'website\pricing.html')

def services(request):
    return render(request, 'website\services.html')