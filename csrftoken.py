import sys
import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'epl.settings')
import django
from django.middleware.csrf import CsrfViewMiddleware, get_token
from django.test import Client

django.setup()
csrf_client = Client(enforce_csrf_checks=True)

URL = ''
USRNM= ''
PASSWORD= ''

csrf_client.get(URL) 
csrftoken = csrf_client.cookies['csrftoken']

login_data = dict(username=USRNM, password=PASSWORD, csrfmiddlewaretoken=csrftoken.value, next='/')
r = csrf_client.post(URL, data=login_data, headers=dict(Referer=URL))