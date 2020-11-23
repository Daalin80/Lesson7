import requests
import datetime
URL = 'http://api.openweathermap.org/data/2.5/forecast/daily'
def return_weather(days=1):
    data = {'q': 'Odesa', 'units': 'metric', 'cnt': days,
            'appid': 'f9ada9efec6a3934dad5f30068fdcbb8'}
    r = requests.get(URL, data)
    return r.json()

result = return_weather(days=5)
with open ('dw.txt', 'w') as f:
    f.writelines(['Day     ', 'Night     ', 'Something ', '\n'])
    for day in result['list']:
        f.writelines([str(day(datetime.datetime.fromtimestamp(dt))) + (5 * ' '),
                     str(day['temp']['day']) + (5 * ' '),
                     str(day['temp']['night']) + (5 * ' '),
                     'Something ', '\n'])
print('done')
