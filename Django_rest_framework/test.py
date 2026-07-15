import urllib.request
from urllib.error import HTTPError

try:
    response = urllib.request.urlopen('http://127.0.0.1:8000/api/hello_spotify/')
    print("Status:", response.status)
    print("Body:", response.read().decode('utf-8'))
except Exception as e:
    print("Error:", e)
