from django.contrib.auth.models import User
from .models import *
from django.shortcuts import redirect
from django.apps import apps
from django.contrib import messages



#---------------$ dashboard search and filtering main function $---------------#
def search(model_name,**filters):
    APP_LABEL = 'auth' if model_name == 'User' else 'store'
    model = apps.get_model(app_label=APP_LABEL, model_name=model_name)
    #- this section to make many filters statments -#
    result = model.objects.none()
    for field, value in filters.items():
        result |= model.objects.filter(**{field:value})
    return result if result.exists() else False



#---------------$ main delete any item of any model $---------------#
def remove_any_item(req,model_name,item_id,direct_page,message_info):
    APP_LABEL = 'auth' if model_name == 'User' else 'store'
    model = apps.get_model(app_label=APP_LABEL, model_name=model_name)
    item = model.objects.get(id=item_id)
    item.delete()
    messages.success(req, f'{message_info} Has Been Removed Successfully.')
    return redirect(direct_page)



#---------------$ main variables class $---------------#
class MainVariable:
    #- return all models data -#
    @classmethod
    def get_data(cls,dataName):
        data = {
            'users':User.objects.all(),
            'products':Products.objects.all(),
            'tags':Tags.objects.all(),
            'blacklist':BlackList.objects.all(),
            'colors':Colors.objects.all(),
            'sizes':Sizes.objects.all(),
            'homemessages':HomeMessages.objects.all(),
            'show_homemessags':HomeMessages.objects.all().first().show_offer_messages if HomeMessages.objects.all() else False,
            'cartsitems':CartItems.objects.all()
            
        }
        return data.get(dataName)


    #- return all models count data -#
    @classmethod
    def counts(cls,dataName):
        data = {
            'users':cls.get_data('users').count(),
            'products':cls.get_data('products').count(),
            'tags':cls.get_data('tags').count()
        }
        return data.get(dataName)


    #- return all models percentage count data -#        
    @classmethod
    def counts_percentage(cls,dataName):
        BLACKLIST_COUNT = cls.get_data('blacklist').count() if cls.get_data('blacklist') is not None else 0
        data = {
            'users':(cls.get_data('users').count() / 20) * 100,
            'products':(cls.get_data('products').count() / 30) * 100,
            'tags':(cls.get_data('tags').count() / 10) * 100,
            'blacklist':(BLACKLIST_COUNT / 10) * 100,
        }
        return data.get(dataName)
    

        
        
        
        

