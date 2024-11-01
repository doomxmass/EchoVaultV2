from django.conf import settings
import requests as REQ

#- checke recaptcha -#
def check_recaptcha(request):
    recaptcha_response = request.POST.get('g-recaptcha-response')
    data = {
    'secret':settings.GOOGLE_RECAPTCHA_SECRET_KEY,
    'response':recaptcha_response
    }
    result = REQ.post('https://www.google.com/recaptcha/api/siteverify',data=data).json()
    return True if result['success'] else False

