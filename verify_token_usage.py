import os
import django
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uroclinic.settings')
django.setup()

client = APIClient()

# Ensure test user exists
username = 'test_token_user_usage'
password = 'test_password'
if not User.objects.filter(username=username).exists():
    user = User.objects.create_user(username=username, password=password)
else:
    user = User.objects.get(username=username)

# Get or create token
token, created = Token.objects.get_or_create(user=user)

# Test 1: Access without token (Should Fail)
client.credentials() # Clear creds
response_anon = client.get('/data/patients/')
if response_anon.status_code == status.HTTP_200_OK:
    print("FAIL: Anonymous access allowed")
else:
    print(f"PASS: Anonymous access blocked ({response_anon.status_code})")

# Test 2: Access with token (Should Pass)
client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
response_auth = client.get('/data/patients/')

if response_auth.status_code == status.HTTP_200_OK:
    print(f"PASS: Token usage successful. Got {len(response_auth.data)} patients.")
else:
    print(f"FAIL: Token access denied. Status: {response_auth.status_code}")
