import requests
import datetime

URL = 'http://api.openweathermap.org/data/2.5/forecast/daily'


def format_value(val):
    if val >= 0:
        result = ' {:.2f}'.format(val)
    else:
        result = '{:.2f}'.format(val)
    return result


def return_weather():
    city_name = input('Введите ваш город: ')
    cnt = input('Введите количество дней: ')
    data = {'q': city_name, 'units': 'metric', 'cnt': cnt,
            'appid': 'f9ada9efec6a3934dad5f30068fdcbb8'}
    r = requests.get(URL, data)
    return r.json()


def weather():
    result = return_weather()
    with open('dw.txt', 'w') as f:
        f.writelines(['Дата\t\t Температура днём\t По ощущениям днём\t Температура ночью', '\n'])
        for day in result['list']:
            f.writelines([datetime.date.fromtimestamp(day['dt']).strftime('%d-%m-%Y') + (8 * ' '),
                          format_value(day['temp']['day']) + (16 * ' '),
                          format_value(day['feels_like']['day']) + (14 * ' '),
                          format_value(day['temp']['night']), '\n'])


weather()
