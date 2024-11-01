from django import forms
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm


#> reset password forms section <#
#---------------$ password reset form $---------------#
#- reset password email form (enter email page) -#
class CustomizedResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'my-custom-form', 
            'placeholder': 'Enter your email address',
        }),
        label=""
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Optionally add custom validation logic
        return email
    

#---------------$ set new password  form $---------------#
#- reset password confirm form (enter new pass and confirm pass) -#
class CustomizedSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'my-custom-form', 
                                        'placeholder': 'Enter your email address',
                                        }),
        label=""
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'my-custom-form', 
                                        'placeholder': 'Enter your email address',
                                        }),
        label=""
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.get('user', None)  # Get the user from kwargs
        super(CustomizedSetPasswordForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        # Call the parent save method to save the new password
        return super().save(commit=commit)
