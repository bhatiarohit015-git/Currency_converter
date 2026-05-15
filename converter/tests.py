from django.test import TestCase
import requests
# Create your tests here.

url = f"https://api.currencyfreaks.com/v2.0/rates/latest?apikey=1d22f72f82bd4552991da204ceb1b210&to=AED&from=INR&amount=100"
response = requests.get(url).json()
print(response)