from django.shortcuts import render, redirect
from .models import Address
from .forms import AddressForm
from django.contrib import messages

# Create your views here.
def home(request):
    all_addresses = Address.objects.all()
    return render(request, 'address_book/home.html',{'all_addresses':all_addresses})

def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Address has been added!'))
            return redirect('home')
        else:
            messages.success(request, ('Seems like there was an error...'))
            return render(request, 'address_book/add_address.html', {})

    else:
        return render(request, 'address_book/add_address.html', {})

def edit_address(request, address_id):
    current_address = Address.objects.get(pk=address_id)
    if request.method == 'POST':
        form = AddressForm(request.POST or None, instance=current_address)
        if form.is_valid():
            form.save()
            messages.success(request, ('Address has been added!'))
            return redirect('home')
        else:
            messages.success(request, ('Seems like there was an error...'))
            return render(request, 'address_book/add_address.html', {})
    else:
        return render(request, 'address_book/edit.html', {'current_address':current_address})

def delete_address(request, address_id):
    current_address = Address.objects.get(pk=address_id)
    current_address.delete()
    messages.success(request, ('Address has been deleted!'))

    return redirect('home')
