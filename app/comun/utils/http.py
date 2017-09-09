from datetime import datetime, timedelta

from django.conf import settings

JWT_EXPIRATION_DELTA = settings.JWT_AUTH['JWT_EXPIRATION_DELTA'].seconds


def set_cookie(self, response, key, value):
	delta = timedelta(seconds=JWT_EXPIRATION_DELTA)
    expires = datetime.strftime(datetime.utcnow() + delta,
    	'%a, %d-%b-%Y %H:%M:%S GMT')
    response.set_cookie(key, value, max_age=JWT_EXPIRATION_DELTA,
        expires=expires, domain=settings.SESSION_COOKIE_DOMAIN,
        secure=settings.SESSION_COOKIE_SECURE or None)