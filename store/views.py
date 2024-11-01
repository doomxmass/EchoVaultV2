from django.shortcuts import render, redirect
from .VARIABLES import MainVariable



#---------------$ home function $---------------#
def home_func(req):

    print(req.user.username)
    
    
    ctx = {
        'is_show_ads':MainVariable.get_data('show_homemessags'),
        'home_messages':MainVariable.get_data('homemessages')
    }
    return render(req, 'app_temps/home.html', ctx)
