from importlib.metadata import files

from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone, Laptop, Watch
from .forms import PhoneForm, LaptopForm, WatchForm


def home(request):
    phones = Phone.objects.all()[:3]
    laptop = Laptop.objects.all()[:3]
    watch = Watch.objects.all()[:3]
    context = {
        "phones" : phones,
        "laptops" : laptop,
        "watches" : watch
    }
    return render(request, 'home.html', context=context)



def phones(request):
    phone = Phone.objects.all()
    context = {
        "phones": phone
    }
    return render(request, 'phones.html', context=context)




def laptops(request):
    laptop = Laptop.objects.all()
    context = {
        "laptops" : laptop
    }
    return render(request, "laptops.html", context=context)



def watchs(request):
    watches = Watch.objects.all()
    context = {
        "watches" : watches
    }
    return render(request, "watchs.html", context=context)




def phone_details(request, pk):
    phone = Phone.objects.get(id=pk)
    context = {
        "phone" : phone,
    }
    return render(request, 'phone_details.html', context=context)




def laptop_details(request, pk):
    laptop = Laptop.objects.get(id=pk)
    context = {
        "laptop" : laptop,
    }
    return render(request, 'laptop_details.html', context=context)



def watch_details(request, pk):
    watch = Watch.objects.get(id=pk)

    context = {
        "watch" : watch,
    }
    return render(request, 'watch_details.html', context=context)


def phone_create_form(request):
    form = PhoneForm(request.POST, request.FILES)
    if form.is_valid():
        phone = form.save()
        return redirect('phone_details', pk=phone.id)
    return render(request, 'phone_create.html', {'form' : form})


def laptop_create_form(request):
    form = LaptopForm(request.POST, request.FILES)
    if form.is_valid():
        laptop = form.save()
        return redirect('laptop_details', pk=laptop.id)
    return render(request, 'laptop_create.html', {'form' : form})



def watch_create_form(request):
    form = WatchForm(request.POST, request.FILES)
    if form.is_valid():
        watch = form.save()
        redirect('watch_details', pk=watch.id)
    return render(request, 'watch_create.html', {'form':form})



def phone_update(request, pk):
    phone = get_object_or_404(Phone, id=pk)
    if request.method == 'POST':
        form = PhoneForm(request.POST, request.FILES, instance=phone)
        if form.is_valid():
            form.save()
            return redirect('phone_details', pk=pk)
    else:
        form = PhoneForm(instance=phone)
    return render(request, 'phone_update.html', {'form':form, 'phone':phone})



def laptop_update(request, pk):
    laptop = get_object_or_404(Laptop, id=pk)
    if request.method == 'POST':
        form = LaptopForm(request.POST, request.FILES, instance=laptop)
        if form.is_valid():
            form.save()
            return redirect('laptop_details', pk=pk)
    else:
        form = LaptopForm(instance=laptop)
    return render(request, 'laptop_update.html', {"form":form, "laptop":laptop})




def watch_update(request, pk):
    watch = get_object_or_404(Laptop, id=pk)
    if request.method == "POST":
        form = WatchForm(request.POST, request.FILES, instance=watch)
        if form.is_valid():
            form.save()
            return redirect('watch_datails', pk=pk)
    else:
        form = WatchForm(instance=watch)
    return render(request, 'watch_update.html', {"form":form, "watch":watch})




def phone_delete(request, pk):
    phone = Phone.objects.get(id=pk)
    if request.method == "POST":
        phone.delete()
        return redirect('phones')
    return render(request, 'phone_delete.html', {'phone' : phone})


def laptop_delete(request, pk):
    laptop = Laptop.objects.get(id=pk)
    if request.method == "POST":
        laptop.delete()
        return redirect('laptops')
    return render(request, 'laptop_delete.html', {'laptop':laptop})

def watch_delete(request, pk):
    watch = Watch.objects.get(id=pk)
    if request.method == "POST":
        watch.delete()
        return redirect('watches')
    return render(request, 'watch_delete.html', {'watch':watch})


