from django.shortcuts import render, redirect
from .models import Phone, Laptop, Watch

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



def phone_create(request):
    if request.method == 'POST':
        phone = Phone()
        phone.name = request.POST.get('name', '')
        phone.price = request.POST.get('price')
        phone.description = request.POST.get('description', '')
        phone.image = request.FILES.get('image')
        phone.save()
        return redirect('phone_details', pk=phone.id)
    return render(request, 'phone_create.html', {'phone' : 'phone'})



def laptop_create(request):
    if request.method == "POST":
        laptop = Laptop()
        laptop.name = request.POST.get('name', "")
        laptop.price = request.POST.get('price', '')
        laptop.description = request.POST.get('description', '')
        laptop.image = request.FILES.get('image')
        laptop.save()
        return redirect("laptop_details", pk=laptop.id)
    return render(request, 'laptop_create.html', {"laptop" : 'laptop'})


def watch_create(request):
    if request.method == "POST":
        watch = Watch()
        watch.name = request.POST.get("name", '')
        watch.price = request.POST.get("price", '')
        watch.description = request.POST.get("description", '')
        watch.image = request.FILES.get("image")
        watch.save()
        return redirect("watch_details", pk=watch.id)
    return render(request, 'watch_create.html', {'watch': "watch"})




def phone_update(request, pk):
    phone = Phone.objects.get(id=pk)
    if request.method == 'POST':
        phone.name = request.POST.get('name', phone.name)
        phone.price = request.POST.get('price', phone.price)
        phone.description = request.POST.get('description', phone.description)
        phone.image = request.FILES.get('image', phone.image)
        phone.save()
        return redirect('phone_details', pk=pk)
    return render(request, 'phone_update.html', {'phone':phone})



def laptop_update(request, pk):
    laptop = Laptop.objects.get(id=pk)
    if request.method == 'POST':
        laptop.name = request.POST.get('name', laptop.name)
        laptop.price = request.POST.get('price', laptop.price)
        laptop.description = request.POST.get('description', laptop.description)
        laptop.image = request.FILES.get('image', laptop.image)
        laptop.save()
        return redirect('laptop_details', pk=pk)
    return render(request, 'laptop_update.html', {'laptop' : laptop})



def watch_update(request, pk):
    watch = Watch.objects.get(id=pk)
    if request.method == "POST":
        watch.name = request.POST.get('name', watch.name)
        watch.price = request.POST.get('price', watch.price)
        watch.description = request.POST.get('description', watch.description)
        watch.image = request.FILES.get('image', watch.image)
        watch.save()
        return redirect('watch_details', pk=pk)
    return render(request, 'watch_update.html', {'watch' : watch})
