
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from soannapp import views
from . import views


urlpatterns = [
    path('',views.index, name='home'),
    path('shop/<str:cname>/', views.shop, name='shop'),
    path('shops/<str:cname>/<str:scname>/', views.shops, name='shops'),
    path('products/<str:cname>/<str:scname>/<str:ccname>/', views.products, name='products'),
    path('details/<str:pname>',views.details, name='details'),
    path('signup/',views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('cart/<int:pid>/', views.cart, name='cart'),
    path('wishlist/',views.wishlist, name='wishlist'),
    path('checkout/',views.checkout, name='checkout'),
    path('about/',views.about, name='about'),
    path('faq/',views.faq, name='faq'),
    path('contact/',views.contact, name='contact'),
    path('logout/',views.logout, name='logout'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
