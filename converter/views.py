from django.shortcuts import render,redirect
import requests
import json
from .models import Currency_converter
API = 'e00dc3fd8136c1430c5cae3e'
# Create your views here.


def converter(request):
    try:
        data = None
        file_path ='converter\\file.json'
        with open(file_path,'r') as file:
            data = json.load(file)
        currency=data['currency']
        currency=dict(sorted(currency.items(), key=lambda item:item[1]))
        converted_amount = None
        if request.method == "POST":
            print(request.POST,"----------------------")
            amount = float(request.POST.get("amount"))
            from_currency = request.POST.get("from_currency")
            to_currency = request.POST.get("to_currency")
            API = "e00dc3fd8136c1430c5cae3e"
            BASE_URL = f"https://v6.exchangerate-api.com/v6/{API}/latest/{from_currency}"
            response = requests.get(BASE_URL)
            print(response)
            if response.status_code == 200:
                data = response.json()
                print(data)
                conversion_rates = data["conversion_rates"]
                if to_currency in conversion_rates:
                    converted_amount = conversion_rates[to_currency]
                    converted_amount = round(amount * converted_amount,2)
                Currency_converter.objects.create(
                    amount = amount,
                    converted_amount = converted_amount,
                    select_currency = from_currency,
                    converted_currency = to_currency
                )
                data = {
                    "amount" : amount,
                    "converted_amount" : converted_amount,
                    "from_currency" : from_currency,
                    "to_currency" : to_currency 
                }
                return render(request, "CONVERTER.HTML", {
            "data" :data,
            "currency":currency
        })
        return render(request, "CONVERTER.HTML", {
            "currency":currency
        })
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return render(request, "CONVERTER.HTML", {
            "currency":currency,
            # "data": None,
            "error": str(e)
        })
    
def all_history(request):
    if request.method == 'GET':
        print(request )
        data = Currency_converter.objects.all()
        return render(request, 'history.html',{"data":data})
    
def clean(request):
    try:
        print(request.method)
        if request.method =='POST':
            data = Currency_converter.objects.all()
            data.delete()
            return render(request, 'history.html')
    except  Exception as e:
        print(str(e))
        return redirect('history')
        