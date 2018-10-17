import requests
from bs4 import beautifulSoup

request = requests.get("http://www.google.com")

print(request.content)
