from django.shortcuts import render



#---------------$ forbidden page $---------------#
def forbidden_func(req):
    return render(req, 'error_temps/forbidden.html')


#---------------$ error 404 page $---------------#
def errro_404_func(req):
    return render(req, 'error_temps/error_404.html')
