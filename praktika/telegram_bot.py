import requests
import json
import telebot


bot = telebot.TeleBot('')

start_txt = 'Привет! \n\nЯ могу сообщить погоду в городе. Просто напиши название города'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, start_txt, parse_mode='Markdown')


def get_weather(city):
    pass
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        "q": city,
        "units": "metric",
        "lang": "ru",
        "appid": "79d1ca96933b0328e1c7e3e7a26cb347"
    }

    try:
        weather_data = requests.get(url, params=params).json()
        weather_data_structure = json.dumps(weather_data, indent=2)
        print(weather_data_structure)

        return weather_data
    except Exception as e:
        print('achtung weather {e}')
        return None


@bot.message_handler(content_types=['text'])
def weather(message):
    city = message.text
    weather_data = get_weather(city)

    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])
    description = weather_data['weather'][0]['description']
    pressure = round(weather_data['main']['pressure'])

    w_now = 'Сейчас в городе ' + city+' ' + \
        str(description)+', '+str(temperature)+' °C'
    w_feels = 'Ощущается как '+str(temperature_feels)+' °C'
    w_pres = 'Атмосферное давление '+str(pressure)+' мм рт.ст.'

    bot.send_message(message.chat.id, w_now)
    bot.send_message(message.chat.id, w_feels)
    bot.send_message(message.chat.id, w_pres)


if __name__ == '__main__':
    print("Бот запущен...")
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            print('achtung!!!! {e}')
