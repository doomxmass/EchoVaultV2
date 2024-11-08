from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


#---------------$ Add new user form $---------------#
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_staff = False
        if commit:
            user.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'input-box','placeholder':' Username'})
        self.fields['email'].widget.attrs.update({'class':'input-box','placeholder':' Email'})
        self.fields['password1'].widget.attrs.update({'class':'input-box','placeholder':' Password'})
        self.fields['password2'].widget.attrs.update({'class':'input-box','placeholder':' Confirm Passwrod'})
        


#---------------$ set admin form $---------------#
class SetAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['is_staff']



#---------------$ home messages form $---------------#
class AddHomeMessagesForm(forms.ModelForm):
    class Meta:
        model = HomeMessages
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddHomeMessagesForm, self).__init__(*args, **kwargs)
        self.fields['customer_service_phone'].widget.attrs.update({'class':'input-box','placeholder':' Servic Phone'})
        self.fields['main_message1'].widget.attrs.update({'class':'input-box','placeholder':' Header Message 1'})
        self.fields['main_message1_description'].widget.attrs.update({'class':'input-box','placeholder':' header message 1 dscription'})
        self.fields['main_message2'].widget.attrs.update({'class':'input-box','placeholder':' Header Message 2'})
        self.fields['main_message2_description'].widget.attrs.update({'class':'input-box','placeholder':' header message 2 dscription'})
        self.fields['main_message3'].widget.attrs.update({'class':'input-box','placeholder':' Header Message 3'})
        self.fields['main_message3_description'].widget.attrs.update({'class':'input-box','placeholder':' header message 3 dscription'})

        self.fields['offer_message1'].widget.attrs.update({'class':'input-box','placeholder':' offer Message 1'})
        self.fields['offer_message1_description'].widget.attrs.update({'class':'input-box','placeholder':' offer message 1 dscription'})
        self.fields['offer_message2'].widget.attrs.update({'class':'input-box','placeholder':' offer Message 2'})
        self.fields['offer_message2_description'].widget.attrs.update({'class':'input-box','placeholder':' offer message 2 dscription'})
        self.fields['offer_message3'].widget.attrs.update({'class':'input-box','placeholder':' offer Message 3'})
        self.fields['offer_message3_description'].widget.attrs.update({'class':'input-box','placeholder':' offer message 3 dscription'})
        self.fields['offer_message4'].widget.attrs.update({'class':'input-box','placeholder':' offer Message 4'})
        self.fields['offer_message4_description'].widget.attrs.update({'class':'input-box','placeholder':' offer message 4 dscription'})

        self.fields['show_offer_messages'].widget.attrs.update({'class':'input-box','placeholder':'show_offer_messages'})
        

#---------------$ blacklist form $---------------#
class HandleBlackList(forms.ModelForm):
    class Meta:
        model = BlackList
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HandleBlackList, self).__init__(*args, **kwargs)
        self.fields['user'].widget.attrs.update({'class':'input-box','placeholder':'Username'})


#---------------$ add product form $---------------#
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        self.fields['tags'].widget.attrs.update({'class':'input-box','placeholder':' Tags'})
        self.fields['colors'].widget.attrs.update({'class':'input-box','placeholder':' Colors'})
        self.fields['sizes'].widget.attrs.update({'class':'input-box','placeholder':' Sizes'})
        self.fields['name'].widget.attrs.update({'class':'input-box','placeholder':' product name'})
        self.fields['bio'].widget.attrs.update({'class':'input-box','placeholder':' Dscription'})
        self.fields['price'].widget.attrs.update({'class':'input-box','placeholder':' Price'})
        self.fields['category'].widget.attrs.update({'class':'input-box','placeholder':' Category'})
        self.fields['image'].widget.attrs.update({'class':'input-box','placeholder':' Image'})
        self.fields['rate'].widget.attrs.update({'class':'input-box','placeholder':' Rating'})



#---------------$ add tag form $---------------#
class AddTagForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddTagForm, self).__init__(*args, **kwargs)
        self.fields['tag'].widget.attrs.update({'class':'input-box','placeholder':' New Tag'})



#---------------$ add color form $---------------#
class AddColorForm(forms.ModelForm):
    class Meta:
        model = Colors
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddColorForm, self).__init__(*args, **kwargs)
        self.fields['color'].widget.attrs.update({'class':'input-box','placeholder':' New Color'})



#---------------$ add size form $---------------#
class AddSizeForm(forms.ModelForm):
    class Meta:
        model = Sizes
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddSizeForm, self).__init__(*args, **kwargs)
        self.fields['size'].widget.attrs.update({'class':'input-box','placeholder':' New Size'})


#---------------$ edt profile form $---------------#
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['nickname'].widget.attrs.update({'class':'input-box','placeholder':' Nickname'})
        self.fields['bio'].widget.attrs.update({'class':'input-box','placeholder':' Bio'})
        self.fields['phone'].widget.attrs.update({'class':'input-box','placeholder':' Phone'})
        self.fields['country'].widget.attrs.update({'class':'input-box','placeholder':' Country'})
        self.fields['city'].widget.attrs.update({'class':'input-box','placeholder':' City'})
        self.fields['image'].widget.attrs.update({'class':'input-box','placeholder':' Image'})
