from django.shortcuts import render, redirect, get_object_or_404
from .VARIABLES import MainVariable,search
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import EditProfileForm
from django.core.mail import send_mail
from env.SecretKeys import AppSecretKey
from threading import Thread
from .decorator import user_is_not_loggedin



#---------------$ home function $---------------#
def home_func(req):
    formal_suits = search('Products',category='Formal Suits')
    business_suts = search('Products',category='Business Casual Suits')
    lounge_suits = search('Products',category='Lounge Suits')
    tuxedos_suits = search('Products',category='Tuxedos')
    
    ctx = {
        #- home messages -#
        'is_show_ads':MainVariable.get_data('show_homemessags'),
        'home_messages':MainVariable.get_data('homemessages'),
        #- suits category filtering -#
        'formal_suits_count': formal_suits.count() if formal_suits else 0,
        'business_suits_count':business_suts.count() if business_suts else 0,
        'lounge_suits_count':lounge_suits.count() if lounge_suits else 0,
        'tuxedos_suits_count':tuxedos_suits.count() if tuxedos_suits else 0,
        'latest_products':list(reversed(MainVariable.get_data('products')))[:4],
    }
    return render(req, 'app_temps/home.html', ctx)


#---------------$ product info function $---------------#
#> if user not logged in <#
@user_is_not_loggedin()
def product_info_func(req,product_id):
    created_message = ''

    selected_product = get_object_or_404(Products,id=product_id)
    user_cart = get_object_or_404(Cart,user=req.user)

    if req.method == 'POST':
        selected_size = req.POST.get('size','m')
        selected_color = req.POST.get('color','black')
        quantity = int(req.POST.get('quantity',1))

        cart_item = CartItems.objects.create(cart=user_cart,
                                            products=selected_product,
                                            color=selected_color,
                                            size=selected_size,
                                            quantity=quantity)
        if cart_item:
            created_message = f'({selected_product.name} - PRODUCT) Added To Your Cart Successfully.'
        else:
            print('not')
            
    
    ctx = {
        'product':selected_product,
        'may_like_products':search('Products',category=selected_product.category),
        'created_message':created_message,
    }
    return render(req, 'app_temps/product_info.html', ctx)


#---------------$ shop function $---------------#
def shop_function(req):
    all_products = MainVariable.get_data('products')

    showing_model = req.GET.get('model')
    if showing_model == 'formal':
        all_products = search('Products',category='Formal Suits')
    elif showing_model == 'business':
        all_products = search('Products',category='Business Casual Suits')
    elif showing_model == 'lounge':
        all_products = search('Products',category='Lounge Suits')
    elif showing_model == 'tuxedos':
        all_products = search('Products',category='Tuxedos')
    else:
        all_products = MainVariable.get_data('products')
    
    
    #- filter section -#
    if req.method == 'POST':
        prices_filters = req.POST.get('price-range')
        colors_filters = req.POST.get('color-type')
        sizes_filters = req.POST.get('size-type')

        #> make sure color and size has a value <#
        color = search('Colors',color=colors_filters)[0] if colors_filters != 'all' else False
        size = search('Sizes',size=sizes_filters)[0] if sizes_filters != 'all' else False

        #: by price color and size :#
        if prices_filters and color and size:
            all_products = Products.objects.filter(Q(price__lte=(float(prices_filters))) & Q(colors=color) & Q(sizes=size))

        #: by price and color :#
        elif prices_filters and color:
            all_products = Products.objects.filter(Q(price__lte=(float(prices_filters))) & Q(colors=color))

        #: by price and size :#
        elif prices_filters and size:
            all_products = Products.objects.filter(Q(price__lte=(float(prices_filters))) & Q(sizes=size))

        #: by color and size :#
        elif color and size:
            all_products = Products.objects.filter(Q(colors=color) & Q(sizes=size))

        #: by price :#
        elif prices_filters:
            all_products = search('Products', price__lte=float(prices_filters))

        #: by color :#
        elif color:
            all_products = search('Products',colors=color)

        #: by size :#
        elif size:
            all_products = search('Products',sizes=size)

    #- pagination section -#
    paginator = Paginator(all_products, 6)
    page_numb = paginator.get_page(req.GET.get('page', 1))

    ctx = {
        'all_products':page_numb,
        'all_colors':MainVariable.get_data('colors'),
        'all_sizes':MainVariable.get_data('sizes'),
        'products_count':MainVariable.get_data('products').count()
    }
    return render(req, 'app_temps/shop.html', ctx)


#---------------$ profilc function $---------------#
#> if user not logged in <#
@user_is_not_loggedin()
def profile_func(req, user_id):
    user = get_object_or_404(User,id=user_id)
    user_profile = get_object_or_404(Profile,user=user)
    cart = get_object_or_404(Cart,user=user)
    cart_items = search('CartItems',cart=cart)

    ctx = {
        'user_profile':user_profile,
        'cart_items_count':cart_items.count() if cart_items else 0,
    }
    return render(req, 'app_temps/profile.html', ctx)


#---------------$ edit profile function $---------------#
#> if user not logged in <#
@user_is_not_loggedin()
def edit_profile_func(req, user_id):
    user = get_object_or_404(User,id=user_id)
    profile = get_object_or_404(Profile,user=user)
    image = profile.image.url

    form = EditProfileForm(instance=profile)
    if req.method == 'POST':
        form = EditProfileForm(req.POST, req.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_page',user.id)
    ctx = {
        'form':form,
        'image':image,
    }
    return render(req, 'app_temps/edit_profile.html', ctx)


#---------------$ Cart function $---------------#
#> if user not logged in <#
@user_is_not_loggedin()
def show_cart_func(req, user_id):
    user = get_object_or_404(User,id=user_id)
    cart = get_object_or_404(Cart,user=user)
    cart_items = search('CartItems',cart=cart)
    subtotal = 0
    if cart_items:
        for item in cart_items:
            total = (item.products.price * item.quantity)
            subtotal += total

    ctx = {
        'cart_items':cart_items if cart_items else [],
        'subtotal':subtotal,
    }
    return render(req, 'app_temps/cart.html', ctx)


#---------------$ delete item from cart $---------------#
#> if user not logged in <#
@user_is_not_loggedin()
def remove_item(req,item_id):
    get_object_or_404(CartItems,id=item_id).delete()
    return redirect('cart_page', req.user.id)


#---------------$ contact function $---------------#
#- send mil function to thread it -#
def send_message_to_gmail(username,email,subject,body):
    try:
        subject = f'{subject} From User : ({username})'
        send_mail(subject,body,AppSecretKey.APP_GMAIL,[email,],fail_silently=False,)
    except Exception as e:
        pass
    

def contact_func(req):
    if req.method == 'POST':
        username = req.POST.get('username',None)
        email = req.POST.get('email',None)
        subject = req.POST.get('subject',None)
        message = req.POST.get('body',None)
        
        Thread(target=send_message_to_gmail,
               kwargs={
                    'username':username,
                    'email':email,
                    'subject':subject,
                    'body':message
                    }).start()

    return render(req, 'app_temps/contact.html')