from django.shortcuts import render

import json

import urllib.request


def index(request):
    if request.method == 'POST':
        city = request.POST['city']



        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=80d4cb5c9d4f85abd8d61494d36d0fb2').read()


        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']),
            "coordinatelat": str(list_of_data['coord']['lat']),
            "temp": str((list_of_data['main']['temp'])-273) + ' Celcius',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data={}
    return render(request, "main/index.html",data)
