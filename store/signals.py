from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail
from env.SecretKeys import AppSecretKey
from threading import Thread
from .models import Cart,Profile,CartItems


'''
#> after seting up signal funtions <#
#> go to apps.py and set <#
from django.apps import AppConfig

class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'your app name'

    def ready(self):
        import store.signals
#> then got to __ini__.py and set <#
default_app_config = 'your app name.apps.StoreConfig'
'''

#---------------$ send success mesage to user gmail when new account $---------------#
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        #- craete cart and profile for user -#
        Cart.objects.create(user=instance)
        Profile.objects.create(user=instance)
        #- send message to user gmail when resister done -#
        def send_message_to_gmail():
            try:
                send_mail(
                    "Email verification From EchVault 2024",
                    f"Hi {instance.username}, You had been sign up a new account in ECHOVAULT app succesfuly.",
                    AppSecretKey.APP_GMAIL, #: from appsecretkeys class  we made :#
                    [instance.email,], #> most be a list <#
                    fail_silently=False,
                    )
            except Exception as e:
                print(f'Error From Signal send_mail \n\n{e}')
    
        #- we made it Thread to me it more fast -#
        Thread(target=send_message_to_gmail,daemon=True).start()



#---------------$ rating signal $---------------#

'''
when any user add a product to his cart SIGNAL automaticlly
will +1 to selected product's rate field
'''
@receiver(post_save, sender=CartItems)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        def rate_added_product():
            added_product = instance.products
            added_product.rate += 1
            added_product.save()
        
        rate_added_product()