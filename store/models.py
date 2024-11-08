from django.db import models
from django.contrib.auth.models import User
from datetime import datetime




#---------------$ sizes model $---------------#
class Sizes(models.Model):
    size = models.CharField(max_length=10,null=True)
    added_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.size


#---------------$ colors model $---------------#
class Colors(models.Model):
    color = models.CharField(max_length=15,null=True)
    added_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.color
    

#---------------$ tags model $---------------#
class Tags(models.Model):
    tag = models.CharField(max_length=15,null=True)
    added_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.tag


#---------------$ products model $---------------#
class Products(models.Model):

    CHOICES = {
        'Formal Suits':'Formal Suits',
        'Business Casual Suits':'Business Casual Suits',
        'Lounge Suits':'Lounge Suits',
        'Tuxedos':'Tuxedos',
    }

    tags = models.ManyToManyField(Tags)
    colors = models.ManyToManyField(Colors)
    sizes = models.ManyToManyField(Sizes)
    
    name = models.CharField(max_length=25, null=True)
    bio = models.TextField(max_length=300, null=True,default='No Descrition.')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=50,null=True, choices=CHOICES)
    image = models.ImageField(upload_to='product/%Y%b%d',
                              default='default_photos/default_product.jpg')
    published_at = models.DateField(auto_now=True)
    rate = models.IntegerField(null=True, default=0)


    def __str__(self):
        return self.name
    
    

#---------------$ Cart model $---------------#
class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


#---------------$ cart items model $---------------#
class CartItems(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    products = models.ForeignKey(Products,on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=100, null=True, default='Black')
    size = models.CharField(max_length=100, null=True, default='M')
    quantity = models.IntegerField(null=True, default=1)

    def __str__(self):
        return self.cart.user.username


#---------------$ profile model $---------------#
#- Function to generate dynamic file path
def user_directory_path(instance, filename):
    #> File will be uploaded to MEDIA_ROOT/<username>/<year><month>/<filename> <#
    username = instance.user.username  #- Assuming there's a user foreign key in your model
    date_path = datetime.now().strftime('%Y-%b-%d')  #- Format as %Y%b%d (like  2024-OCT-01)
    return f'users/{username}/{date_path}/{filename}'


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nickname = models.CharField(max_length=14, null=True, default='User')
    bio = models.TextField(max_length=150, null=True, default='Empty!')
    phone = models.CharField(max_length=20, null=True , default='*** *** *****')
    country = models.CharField(max_length=40, null=True, blank=True, default='Unknown')
    city = models.CharField(max_length=40, null=True, blank=True, default='Unknown')
    image = models.ImageField(upload_to=user_directory_path,
                              default='default_photos/default_user.png')
    

    def __str__(self):
        return self.user.username


#---------------$ black lsit USERS model $---------------#
class BlackList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blocked_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username
    
    @classmethod
    def blacklist(cls):
        return BlackList.objects.all() if list(BlackList.objects.all()) else None
    
    @classmethod
    def is_in_blacklist(cls,useremail:str):
        blocked_users = BlackList.objects.all()
        for info in blocked_users:
            if useremail == info.user.email:
                return True
        else:
            return None


#---------------$ homem essages $---------------#
class HomeMessages(models.Model):
    customer_service_phone = models.CharField(max_length=15,null=True)
    main_message1 = models.CharField(max_length=15,null=True)
    main_message1_description = models.TextField(max_length=100,null=True)
    main_message2 = models.CharField(max_length=15,null=True)
    main_message2_description = models.TextField(max_length=100,null=True)
    main_message3 = models.CharField(max_length=15,null=True)
    main_message3_description = models.TextField(max_length=100,null=True)

    offer_message1 = models.CharField(max_length=15,null=True)
    offer_message1_description = models.CharField(max_length=15,null=True)
    offer_message2 = models.CharField(max_length=15,null=True)
    offer_message2_description = models.CharField(max_length=15,null=True)
    offer_message3 = models.CharField(max_length=15,null=True)
    offer_message3_description = models.CharField(max_length=15,null=True)
    offer_message4 = models.CharField(max_length=15,null=True)
    offer_message4_description = models.CharField(max_length=15,null=True)

    show_offer_messages = models.BooleanField(null=True, default=True, choices={True:'Show',False:'Hide'})