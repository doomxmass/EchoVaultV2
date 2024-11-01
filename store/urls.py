from django.urls import path
from . import views
from . import signup_login_logout_views
from .costum_reset_password_forms_templates import *
from . import admin_views
from .VARIABLES import remove_any_item


urlpatterns = [
    #---------------$ homepage $---------------#
    path('', views.home_func, name='home_page'),
    #---------------$ login signup sectio $---------------#
    #- social login check blacklist -#
    path('sociallogin/', signup_login_logout_views.sociallogin_check, name='sociallogin_page'),
    path('accounts/3rdparty/signup/', signup_login_logout_views.sociallogin_signup, name='exist_email_page'),
    #- login url -#
    path('accounts/login/', signup_login_logout_views.login_func, name='login_page'),
    #- register url -#
    path('accounts/signup/', signup_login_logout_views.register_func, name='registr_page'),
    #- logout url -#
    path('accounts/logout/', signup_login_logout_views.logout_func, name='logout_page'),
    #- black list link (forbidden users) -#
    path('forbidden/', signup_login_logout_views.forbidden_func, name='forbidden_page'),
    #---------------$ reset password lins $---------------#
    #: my custom reset password pages :#
    path('password/reset', CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<str:uidb64>/<str:token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #> after this dont forget to go to admin dashboard and in sites section change example.com to localhost:8000 <#
    #---------------$ ADMIN DASHBOARD link [admin] $---------------#
    #- dashboard link -#
    path('dashboard/', admin_views.dashboard_func, name='dashboard_page'),
    #- add home messages link -#
    path('home/messages/', admin_views.home_messages_func, name='home_messages_page'),
    #---------------$ black list [admin] $---------------#
    #- black list link -#
    path('blacklist/', admin_views.blacklist_func, name='blacklist_page'),
    #- delete from blacklist link -#
    path('remove/blacklist/<str:user_id>/<str:page_name>/',
         admin_views.remove_form_blacklist_func, name='remove_blacklist'),
    #---------------$ remove link for all models [admin] $---------------#
    #> main delete link <#
    path('remove/item/<str:model_name>/<str:item_id>/<str:direct_page>/<str:message_info>/',
        remove_any_item, name='main_remove_link'),
    #---------------$ users [admin] $---------------#
    #- add user link -#
    path('add-user/', admin_views.add_user_func, name='add_user_page'),
    #---------------$ prducts [admin] $---------------#
    #- add product link -#
    path('add-product/', admin_views.add_product_func, name='add_product_page'),
    #- product details -#
    path('product/details/<str:product_id>',
         admin_views.product_details_func, name='product_details_page'),
    #- edit product link -#
    path('edit-product/<str:product_id>/<str:page_name>/', admin_views.edit_product_func, name='edit_product_page'),
    #---------------$ tags [admin] $---------------#
    #- add tag link -#
    path('add-tag/', admin_views.add_tag_func, name='add_tag_page'),
    #---------------$ colors [admin] $---------------#
    #- add color link -#
    path('add-color/', admin_views.add_color_func, name='add_color_page'),
    #---------------$ sizes [admin] $---------------#
    #- add size link -#
    path('add-size/', admin_views.add_size_func, name='add_size_page'),
    #---------------$ admns list [admin] $---------------#
    #- admins list link -#
    path('admins/list/', admin_views.admin_list_func, name='admins_list_page'),
    #- add admin link -#
    path('admins/add/', admin_views.add_admin_func, name='add_admin_page'),
    #- set admin link -#
    path('admins/set/<str:user_id>', admin_views.set_admin_func, name='set_admin_page'),
    #- set normal user link -#
    path('admins/unset/<str:user_id>', admin_views.unset_admin_func, name='unset_admin_page'),
]
