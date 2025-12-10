from django.shortcuts import render
import requests
import datetime

def index(request):
    if request.method == "POST":
        city = request.POST.get('city', 'Dhaka')
    else:
        city = 'Dhaka'

    apiID = '71ff029011f492ab0add8b257f211d89'
    apiUrl = 'https://api.openweathermap.org/data/2.5/weather'
    PARMS = {'q': city, 'appid': apiID, 'units': 'metric'}

    r = requests.get(url=apiUrl, params=PARMS)
    res = r.json()

    des = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    day = datetime.date.today()

    data = {
        'des': des,
        'icon': icon,
        'temp': temp,
        'day': day,
        'city': city
    }

    return render(request, 'weatherapp/index.html', data)
