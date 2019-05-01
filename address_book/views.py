from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'address_book/home.html',{})

def add_address(request):
    return render(request, 'address_book/add_address.html',{})
