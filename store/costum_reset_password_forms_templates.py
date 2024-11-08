from .custome_resret_password_forms import (CustomizedResetPasswordForm,
                                    CustomizedSetPasswordForm)
#- to customize password reset form -#
from django.contrib.auth.views import (PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)



#---------------$ reset password function $---------------#
#- reset password main page -#
class CustomPasswordResetView(PasswordResetView):
    form_class = CustomizedResetPasswordForm
    template_name = 'change_pass_temps/change_password.html'


#- reset password done page -#
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'change_pass_temps/change_password_done.html'


#- reset pssword confirm page -#
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomizedSetPasswordForm
    template_name = 'change_pass_temps/change_password_confirm.html'


#- reset pssword complete page -#
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'change_pass_temps/change_password_complete.html'

