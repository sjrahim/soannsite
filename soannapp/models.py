from django.db import models
from django.db.models.fields import AutoField
from django.contrib.auth.models import User
from datetime import datetime





# Create your models here.

class Category(models.Model):
    catname = models.CharField(max_length=150) 
    slug = models.SlugField(max_length=60, unique=True, null=True)
    
    
    def __str__(self):
       return (self.catname)


    

class Subcategory(models.Model):
    category = models.ForeignKey(Category, related_name='children',  on_delete=models.CASCADE)
    subcatname = models.CharField(max_length=100)
    slug = models.SlugField(max_length=60, unique=True, null=True)

    def __str__(self):
       return "%s " % (self.subcatname)

class Childcategory(models.Model):
    category = models.ForeignKey(Category, related_name='childrencat',  on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name='subcategorychild',  on_delete=models.CASCADE)
    childcatname = models.CharField(max_length=100)
    slug = models.SlugField(max_length=60, unique=True, null=True)

    def __str__(self):
       return self.childcatname

class Country(models.Model):
    countryname = models.CharField(max_length=200)

    def __str__(self):
        return  self.countryname

class Suppliers(models.Model):
    companyname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=70)
    lastname = models.CharField(max_length=70)
    address = models.CharField(max_length=250, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='allcountry')
    mobile = models.IntegerField(null=True, blank=True)
    fax = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=150, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return " %s   -   %s  -  %s" % (self.companyname, self.mobile, self.email)

class Quantity(models.Model):
    quantityname = models.CharField(max_length=100)

    def __str__(self):
        return self.quantityname

class Weight(models.Model):
    weightname = models.CharField(max_length=100)

    def __str__(self):
        return self.weightname

class productstatus(models.Model):
    pvname = models.CharField(max_length=80)

    def __str__(self):
        return self.pvname

class Product(models.Model):
    productsku = models.CharField(max_length=100)
    suppliers = models.ForeignKey(Suppliers, related_name='psupliers', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='pcategory', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name='psubcategory', on_delete=models.CASCADE)
    childcategory = models.ForeignKey(Childcategory, related_name='pchildcategory', on_delete=models.CASCADE)
    productname = models.CharField(max_length=250)
    pslag = models.SlugField(max_length=200, null=True, blank=True)
    quantitystock = models.IntegerField()
    quantity = models.ForeignKey(Quantity, related_name='pquantity', on_delete=models.CASCADE)
    purchaseprice = models.DecimalField(max_digits=12, decimal_places=2)
    sellprice = models.DecimalField(max_digits=12, decimal_places=2)
    discountprice = models.DecimalField(max_digits=12, decimal_places=2)
    weightunit =models.IntegerField()
    weight = models.ForeignKey(Weight, related_name='pweight', on_delete=models.CASCADE)
    productdetails = models.TextField(max_length= 500, blank=True)
    specification = models.TextField(max_length= 500, blank=True)
    unitorder = models.IntegerField(blank=True, null=True)
    currentdt = models.DateField()
    updatedt = models.DateField(blank=True, null=True)
    productstatus = models.ForeignKey(productstatus, related_name='pv', on_delete=models.CASCADE, null=True, blank=True)
    liveproduct = models.BooleanField(default=False)

    def __str__(self):
        return " %s   -   %s   -   %s" % (self.productname, self.sellprice, self.discountprice)
    
class Image(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    product = models.ForeignKey(Product, related_name='imgproduct', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='')
    imageactive = models.SmallIntegerField(null=True)

    def __str__(self):
        return self.title

class Customer(models.Model):
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=30, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=5, null=True, blank=True)
    currentdt = models.DateTimeField(default=datetime.now, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s %s" % (self.firstname, self.lastname, self.email )

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
