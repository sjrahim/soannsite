from django.contrib import admin
from soannapp.models import Category, Childcategory, Country, Customer, Image, Product, Quantity, Subcategory, Suppliers, Weight, productstatus

# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('catname', )}

class subcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('subcatname', )}

class childcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('childcatname', )}

class productnameAdmin(admin.ModelAdmin):
    prepopulated_fields={'pslag': ('productname', )}
    
    
    


admin.site.register(Image),
admin.site.register(Product, productnameAdmin),
admin.site.register(Category, categoryAdmin),
admin.site.register(Subcategory, subcategoryAdmin),
admin.site.register(Childcategory, childcategoryAdmin),
admin.site.register(Country),
admin.site.register(Suppliers),
admin.site.register(Quantity),
admin.site.register(Weight),
admin.site.register(productstatus),
admin.site.register(Customer)
