from django.shortcuts import render
from django.http import HttpResponse
from .models import product, contact
from math import ceil

# Create your views here.

def index(request):
    #products=product.objects.all()
   # print(products)
    #params = {'product':products,'no_of_slide':4, 'range':4}
    allProds = []
    catprods = product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod,  nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contactfun(request):
    if request=='POST':
        print(request)
    email1=request.POST.get('email','')
    text1=request.POST.get('text','')
    print(email1,text1)
    contact1=contact(email=email1, text=text1)
    contact1.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    return HttpResponse("tracker")

def search(request):
    return HttpResponse("search")

def productview(request,myid):
    product1 = product.objects.filter(id=myid)
    print(product1)
    return render(request, 'shop/prodview.html', {'product1':product1[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')




