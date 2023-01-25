from django.shortcuts import render, redirect
from django.views import View
from .models import Product, Customer, Cart
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q


# Create your views here.
def home(request):
    return render(request, "app/home.html")


def about(request):
    return render(request, "app/about.html")


def contact(request):
    return render(request, "app/contact.html")


class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html", locals())


class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, "app/category.html", locals())


class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, "app/product_detail.html", locals())


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, "app/customer_registration.html", locals())
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Register Succesfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, "app/customer_registration.html", locals())


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            locality = form.cleaned_data['locality']
            zipcode = form.cleaned_data['zipcode']
            city = form.cleaned_data['city']

            reg = Customer(user=user, name=name, mobile=mobile, locality=locality, zipcode=zipcode, city=city)
            reg.save()
            messages.success(request, "Congratulations! Profile Save Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'app/profile.html', locals())

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', locals())


class updateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'app/updateAddress.html', locals())

    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.mobile = form.cleaned_data['mobile']
            add.locality = form.cleaned_data['locality']
            add.zipcode = form.cleaned_data['zipcode']
            add.city = form.cleaned_data['city']
            add.save()

            messages.success(request, "Congratulations! Profile Save Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect("address")

#### Jeigu noreciau , kad ta pati preke tik kitos spalvos ideti i krepseli
# def add_to_cart(request):
#     user = request.user
#     product_id = request.GET.get('prod_id')
#     if Cart.objects.filter(product=product_id).exists():
#         prod_id = request.GET['prod_id']
#         c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
#         c.quantity += 1
#         c.save()
#         user = request.user
#         cart = Cart.objects.filter(user=user)
#         amount = 0
#         for p in cart:
#             value = p.quantity * p.product.discounted_price
#             amount = amount + value
#         totalamount = amount + 3.50
#         print(prod_id)
#         data = {
#             'quantity': c.quantity,
#             'amount': amount,
#             'totalamount': totalamount
#         }
#         return redirect('/cart')
#     else:
#         pass
#         product = Product.objects.get(id=product_id)
#         Cart(user=user, product=product).save()
#         return redirect('/cart')

# arba

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')


def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 3.50
    return render(request, 'app/addtocart.html', locals())



class checkout(View):
    def get(self, request):
        return render(request, 'app/checkout.html', locals())


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 3.50
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)



def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 3.50
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)



def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 3.50
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)