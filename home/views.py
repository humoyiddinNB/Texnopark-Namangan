from django.shortcuts import render
from .models import Phone, Laptop, Watch

def home(request):
    phones = Phone.objects.all()
    laptop = Laptop.objects.all()
    watch = Watch.objects.all()
    return render(request, 'home.html', {"phones": phones, 'laptops' : laptop, 'watches' : watch})