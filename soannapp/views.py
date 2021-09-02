from django.http import  HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from soannapp.models import Category, Childcategory, Customer, Product, Subcategory, Image, Customer
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password



# Create your views here.


def index(request):
    
    if request.session.has_key('custid'):
        custid = request.session['custid']
        lastname = request.session['lastname']
    else:
        custid = ""
        lastname = ""
    catlist = Category.objects.all()
    subcategory = Subcategory.objects.all()
    childcategory = Childcategory.objects.all()
    products = Product.objects.all().order_by('id')[:12]
    picture = Image.objects.all()
    
    context= {'cat':catlist , 'subcategory':subcategory, 'products':products, 'picture':picture, 'custid': custid, 'lastname': lastname, 'childcategory': childcategory}
    return render(request,'index.html', context)

def shop(request, cname):
    if request.session.has_key('custid'):
        custid = request.session['custid']
        lastname = request.session['lastname']
    else:
        custid = ""
        lastname = ""
    products = Product.objects.all()
    catlist = Category.objects.all()
    subcategory = Subcategory.objects.all()
    picture = Image.objects.all()
    catslug = Category.objects.get(slug=cname)   
    context= {'cat':catlist, 'subcategory':subcategory, 'product':products, 'catslug':catslug, 'picture':picture, 'custid': custid, 'lastname': lastname}
    return render(request,'shop.html', context)

def shops(request, cname, scname):
    if request.session.has_key('custid'):
        custid = request.session['custid']
        lastname = request.session['lastname']
    else:
        custid = ""
        lastname = ""
    products = Product.objects.all()
    catlist = Category.objects.all()
    subcategory = Subcategory.objects.all()
    picture = Image.objects.all()
    catslug = Category.objects.get(slug=cname)  
    scatslug = Subcategory.objects.get(slug=scname)   
    context= {'cat':catlist, 'subcategory':subcategory, 'product':products, 'catslug':catslug, 'scatslug':scatslug, 'picture':picture, 'custid': custid, 'lastname': lastname}
    return render(request,'shops.html', context)

def products(request, cname, scname, ccname):
    if request.session.has_key('custid'):
        custid = request.session['custid']
        lastname = request.session['lastname']
    else:
        custid = ""
        lastname = ""
    products = Product.objects.all()
    catlist = Category.objects.all()
    subcategory = Subcategory.objects.all()
    childcategory = Childcategory.objects.all()
    picture = Image.objects.all()
    catslug = Category.objects.get(slug=cname)  
    scatslug = Subcategory.objects.get(slug=scname)
    ccslug =   Childcategory.objects.get(slug=ccname)
    context= {'cat':catlist, 'subcategory':subcategory, 'childcategory':childcategory, 'product':products, 'catslug':catslug, 'scatslug':scatslug,'ccslug':ccslug, 'picture':picture, 'custid': custid, 'lastname': lastname}
    return render(request,'products.html', context)


def details(request, pname):
    if request.session.has_key('custid'):
        custid = request.session['custid']
        lastname = request.session['lastname']
    else:
        custid = ""
        lastname = ""
    catlist = Category.objects.all()
    subcategory = Subcategory.objects.all()
    products = Product.objects.get(pslag=pname)
    picture = Image.objects.all()
    context= {'cat':catlist , 'subcategory':subcategory, 'products':products, 'picture':picture, 'custid': custid, 'lastname': lastname}
    return render(request,'product_details.html', context)

def signup(request):
    if request.method == "POST":
        if  request.POST.get('email') and request.POST.get('password'):
            redirectTo = request.POST.get('next', '')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            passworden = request.POST.get('password')
            password= make_password(passworden)
            if Customer.objects.filter(email=email).exists():
                messages.warning(request, 'Email Address Already Exists')
                return render(request, 'index.html')
            else:
                saverecord = Customer(firstname=firstname, lastname=lastname, email=email, password=password)
                saverecord.save()
                messages.success(request, 'Your sign up sccessfully')
                send_mail('Customer account confirmation', '<h4>SOANN</h4><br><br> Welcome to SOANN <br><br> You have activated your customer account. Next time you shop with us, log in for faster checkout. <br><br>If you have any questions, reply to this email or contact us at sjrahim@gmail.com', 'sjrahim@gmail.com', ['shahin@archiana.com'])
                return HttpResponseRedirect(redirectTo)
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def login(request):
     
     if request.method == "POST":
        redirectTo = request.POST.get('next', '')
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        if customer:
           flag =  check_password(password, customer.password)
           if flag:
               messages.success(request, 'Your sign in sccessfully')
               request.session['firstname'] = customer.firstname
               request.session['lastname'] = customer.firstname
               request.session['custid'] = customer.id
               return HttpResponseRedirect(redirectTo)
           else:
                messages.warning(request, 'Email and Password Invalid!!')
                return HttpResponseRedirect(redirectTo)
        else:
            messages.warning(request, 'Email and Password Invalid!!')
            return HttpResponseRedirect(redirectTo)
     else:
        messages.warning(request, 'Email and Password Invalid!!')
        return render(request, 'index.html')


def logout(request):
    del request.session['custid']
    del request.session['firstname']
    del request.session['lastname']
    return redirect('/')

def cart(request, pid):
    
    cart = request.session.get('cart')
    if cart:
        quantity = cart.get(pid)
        if quantity:
            cart[quantity] = quantity + 1
        else:
            cart[pid] = 1
    else:
        cart = { }
        cart[pid] = 1
    
    request.session['cart'] = cart
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def wishlist(request):
    catlist = Category.objects.all()
    subcategory = Subcategory.objects.all()
    context= {'cat':catlist , 'subcategory':subcategory}
    return render(request,'wish_list.html', context)

def checkout(request):
    catlist = Category.objects.all()
    subcategory = Subcategory.objects.all()
    context= {'cat':catlist , 'subcategory':subcategory}
    return render(request,'checkout.html', context)

def about(request):
    catlist = Category.objects.all()
    subcategory = Subcategory.objects.all()
    context= {'cat':catlist , 'subcategory':subcategory}
    return render(request,'about.html', context)

def faq(request):
    catlist = Category.objects.all()
    subcategory = Subcategory.objects.all()
    context= {'cat':catlist , 'subcategory':subcategory}
    return render(request,'faq.html', context)

def contact(request):
    catlist = Category.objects.all()
    subcategory = Subcategory.objects.all()
    context= {'cat':catlist , 'subcategory':subcategory}
    return render(request,'contact.html', context)