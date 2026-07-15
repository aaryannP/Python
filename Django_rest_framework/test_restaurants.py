import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_rest_framework.settings")
django.setup()

from django.test import Client

c = Client()

# Create using APIView
print("--- Creating via APIView ---")
resp = c.post('/restaurants/apiview/', {'name': 'Pizza Hut', 'cuisine': 'Italian', 'rating': 4.5})
print(resp.status_code, resp.json())

# List using GenericAPIView
print("--- Listing via GenericAPIView ---")
resp = c.get('/restaurants/generic/')
print(resp.status_code, resp.json())

# Update via APIView
print("--- Updating via APIView ---")
resp = c.patch('/restaurants/apiview/1/', {'rating': 4.8}, content_type='application/json')
print(resp.status_code, resp.json())

# Delete via GenericAPIView
print("--- Deleting via GenericAPIView ---")
resp = c.delete('/restaurants/generic/1/')
print(resp.status_code)
