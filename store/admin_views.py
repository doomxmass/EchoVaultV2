from .VARIABLES import MainVariable,search
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages


#---------------$ dashboard function $---------------#
def dashboard_func(req):
    all_users = MainVariable.get_data('users')
    all_products = MainVariable.get_data('products')
    blacklist_info = MainVariable.get_data('blacklist')
    all_tags = MainVariable.get_data('tags')
    all_colors = MainVariable.get_data('colors')
    all_sizes = MainVariable.get_data('sizes')
    sales = 0
    for i in MainVariable.get_data('cartsitems'):
        sales += i.products.price


    #- search section -#
    if req.method == 'POST':
        search_in = req.POST.get('flexRadioDefault')
        search_value = req.POST.get('search-value')

        if search_in == 'users-search':
            filtered = search('User',username__icontains=search_value,
                                    email__icontains=search_value)
            if filtered:
                all_users = filtered
        elif search_in == 'product-search':
            #> make sure the search value is integer to search in prices <#
            if search_value.isdigit():
                filtered = search('Products',price__icontains=int(search_value))
            else:
                filtered = search('Products',name__icontains=search_value,
                                            category__icontains=search_value)
            if filtered:
                all_products = filtered
        elif search_in == 'tags-search':
            filtered = search('Tags',tag__icontains=search_value)
            if filtered:
                all_tags = filtered
        elif search_in == 'colors-search':
            filtered = search('Colors',color__icontains=search_value)
            if filtered:
                all_colors = filtered

    ctx = {
        'users_count':MainVariable.counts('users'),
        'products_count':MainVariable.counts('products'),
        'tags_count':MainVariable.counts('tags'),
        'sales':sales,
        'user_prog':MainVariable.counts_percentage('users'),
        'products_prog':MainVariable.counts_percentage('products'),
        'tags_prog':MainVariable.counts_percentage('tags'),
        'blacklist_prog':MainVariable.counts_percentage('blacklist'),
        'all_users':all_users,
        'all_products':all_products,
        'blacklist_info':blacklist_info,
        'all_tags':all_tags,
        'all_colors':all_colors,
        'all_sizes':all_sizes,
    }
    return render(req, 'admin_temps/dashboard.html', ctx)



#---------------$ home messsages funtion $---------------#
def home_messages_func(req):
    form = AddHomeMessagesForm()
    if req.method == 'POST':
        form = AddHomeMessagesForm(req.POST)
        if form.is_valid():
            #- clear all old messages then save the new messages -#
            MainVariable.get_data('homemessages').delete()
            form.save()
            return redirect('dashboard_page')
    ctx = {
        'home_messages_form':form
    }
    return render(req, 'admin_temps/home_messages.html', ctx)


#---------------$ black list function $---------------#
def blacklist_func(req):
    message_alert = ''
    message_success = ''
    form = HandleBlackList()
    if req.method == 'POST':
        form = HandleBlackList(req.POST)
        if form.is_valid():
            #- check if user in blacklist -#
            user_id = req.POST.get('user')
            user = get_object_or_404(User, id=user_id)
            if not BlackList.objects.filter(user=user).exists():
                form.save()
                message_success = f'USER : ( {user.username} - {user.email} ) Added To BlackList.'
            else:
                message_alert = f'USER : ( {user.username} - {user.email} )  Already Exists in BlackList!'
    ctx = {
        'blacklist_form':form,
        'blacklist_info':MainVariable.get_data('blacklist'),
        'message_success':message_success,
        'message_alert':message_alert,
    }
    return render(req,'admin_temps/blacklist.html', ctx)


#: remove an user from black list function :#
def remove_form_blacklist_func(req,user_id,page_name):
    user = get_object_or_404(User, id=user_id)
    blocked_user = BlackList.objects.filter(user=user)
    blocked_user.delete()
    messages.success(req, f'User : {user.username} - {user.email} Removed From Blacklist.')
    if page_name == 'blacklist':
        return redirect('blacklist_page')
    elif page_name == 'dashboard':
        return redirect('dashboard_page')


#---------------$ add user function $---------------#
def add_user_func(req):
    form = RegisterUserForm()
    exist_email_message = ''
    success_message = ''
    if req.method == 'POST':
        form = RegisterUserForm(req.POST)
        username = req.POST.get('username')
        email = req.POST.get('email')
        exist_email = User.objects.filter(email=email).exists()
        exist_username = User.objects.filter(username=username).exists()
        if not exist_email and not exist_username:
            if form.is_valid():
                form.save()
                success_message = f'(User : {username} - {email} Has Been Added Successfully. )'
        else:
            exist_email_message = f'{email} Already Used!'
    ctx = {
        'all_users':MainVariable.get_data('users'),
        'adduser_form':form,
        'exist_email_message':exist_email_message,
        'success_message':success_message,
    }
    return render(req,'admin_temps/add_user.html',ctx)


#---------------$ add product function $---------------#
def add_product_func(req):
    form = AddProductForm()
    success_message = ''
    if req.method == 'POST':
        form = AddProductForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            success_message = 'New Product Has Been Added Successfully.'
    ctx = {
        'addproduct_form':form,
        'all_products':MainVariable.get_data('products'),
        'success_message':success_message,
    }
    return render(req, 'admin_temps/add_product.html', ctx)


#---------------$ product details function $---------------#
def product_details_func(req,product_id):
    ctx = {
        'product':get_object_or_404(Products,id=product_id),
    }
    return render(req, 'admin_temps/detail.html', ctx)


#---------------$ edit product function $---------------#
def edit_product_func(req,product_id,page_name):
    product = get_object_or_404(Products,id=product_id)
    form = AddProductForm(instance=product)
    if req.method == 'POST':
        form = AddProductForm(req.POST, req.FILES,instance=product)
        if form.is_valid():
            form.save()
            messages.success(req, f'{product.name} Changes Ha Been Saved.')
            if page_name == 'dashboard':
                return redirect('dashboard_page')
            if page_name == 'add product':
                return redirect('add_product_page')
    ctx = {
        'editProduct_form':form,
        'product_image':product
    }
    return render(req, 'admin_temps/edit_product.html', ctx)


#---------------$ add tag funcion $---------------#
def add_tag_func(req):
    form = AddTagForm()
    if req.method == 'POST':
        form = AddTagForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'New Tag Has Been Added Successfully.')
            return redirect('add_tag_page')
    ctx = {
        'all_tags':MainVariable.get_data('tags'),
        'addTag_form':form
    }
    return render(req, 'admin_temps/add_tag.html', ctx)


#---------------$ add color funcion $---------------#
def add_color_func(req):
    form = AddColorForm()
    if req.method == 'POST':
        form = AddColorForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'New Color Has Been Added Successfully.')
            return redirect('add_color_page')
    ctx = {
        'all_colors':MainVariable.get_data('colors'),
        'addColor_form':form
    }
    return render(req, 'admin_temps/add_color.html', ctx)


#---------------$ add size funcion $---------------#
def add_size_func(req):
    form = AddSizeForm()
    if req.method == 'POST':
        form = AddSizeForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'New Size Has Been Added Successfully.')
            return redirect('add_size_page')
    ctx = {
        'all_sizes':MainVariable.get_data('sizes'),
        'addSize_form':form
    }
    return render(req, 'admin_temps/add_size.html', ctx)


#---------------$ admins list funtion $---------------#
def admin_list_func(req):
    ctx = {
        'all_users':MainVariable.get_data('users'),
    }
    return render(req, 'admin_temps/admins_list.html', ctx)


#---------------$ add admin funtion $---------------#
def add_admin_func(req):
    all_users = MainVariable.get_data('users')
    if req.method == 'POST':
        search = req.POST.get('search')
        #- __icontains to get all objects if any letter in usernames or email -#
        all_users = User.objects.filter(username__icontains=search) | User.objects.filter(email__icontains=search)
    
    ctx = {
        'all_users':all_users,
    }
    return render(req, 'admin_temps/add_admin.html', ctx)


#---------------$ set admin funtion $---------------#
def set_admin_func(req,user_id):
    user = get_object_or_404(User,id=user_id)
    form = SetAdminForm(instance=user)
    user = form.save(commit=False)
    user.is_staff = True
    user.save()
    messages.success(req, f'{user.username} - Became Manager Successfully!')
    return redirect('add_admin_page')


#---------------$ set admin funtion $---------------#
def unset_admin_func(req,user_id):
    user = get_object_or_404(User,id=user_id)
    form = SetAdminForm(instance=user)
    user = form.save(commit=False)
    user.is_staff = False
    user.save()
    messages.success(req, f'{user.username} - Removed From Managers List!')
    return redirect('admins_list_page')


