from django.shortcuts import render,redirect
from.models import Vendor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from.forms import ProductForm
from apps.product.models import Product
from django.utils.text import slugify

# Create your views here.
def become_vendor(request):
    if request.method=='GET':
            form=UserCreationForm()
            return render(request,'authentication/become_vendor.html',{'form':form})
    else:
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            vendor=Vendor.objects.create(user=user,name=user.username)
            messages.success(request ,'Vendor account created successfully')
            return redirect('vendor_admin')


@login_required()
def vendor_admin(request):
    vendor = request.user.vendor
    products = vendor.products.all()
    return render(request,'vendor/vendor_panel.html',{'vendor': vendor,'products': products })



@login_required()
def add_product(request,id=0):
    vendor=request.user.vendor

    if request.method=='GET':
        if id==0:
            form=ProductForm()
        else:
            prdct=vendor.products.get(pk=id)
            form=ProductForm(instance=prdct)
            return render(request,'vendor/add_product.html',{'form':form})
    else:
        if id==0:
            form=ProductForm(request.POST,request.FILES)              #Explain
            messages.success(request,'Product added successfully')
        else:
            prdct = vendor.products.get(pk=id)
            form= ProductForm(request.POST,request.FILES,instance=prdct)
            messages.success(request,'Product updated successfully')

    if form.is_valid():
        prdct=form.save(commit=False)
        prdct.vendor=request.user.vendor
        prdct.slug=slugify(prdct.title)
        prdct.save()
        return redirect('vendor_admin')



def delete_product(request,id):
    prdct = vendor.products.get(pk=id)
    prdct.delete()
    messages.success(request,'Product deleted successfully')
    return redirect('vendor_admin')
































