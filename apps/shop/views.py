from django.shortcuts import render, redirect
from .models import Product

def index(request):
    context={
        'items': Product.objects.all().values()
    }
    if 'total' not in request.session:
        request.session['total']=0
    return render(request, 'shop/index.html', context)
def buy(request):
    itemid=request.POST['hidden']
    print(itemid)
    item=Product.objects.all().values().get(id=itemid)
    quantity=request.POST['quantity']
    price = item['price']*int(quantity)
    request.session['itemid']=itemid
    request.session['quantity']=quantity
    request.session['price']=price
    request.session['total']+=price
    return redirect('/amadon/checkout')
def checkout(request):
    x=Product.objects.all().values().get(id=request.session['itemid'])
    name=x['name']
    context={
        'name':name,
        'quantity':request.session['quantity'],
        'price':request.session['price']
    }
    return render(request, 'shop/checkout.html', context)