

import telebot
import numpy as np
from scipy.signal import find_peaks
import math
import requests
import os
import json
import matplotlib.pyplot as plt
import io

flags = ['/rev', '/exc']
API_TOKEN = '7851183070:AAFqfoPQ5TXY_5oxeboVR532bkpNLvfUinA'
bot = telebot.TeleBot(API_TOKEN)
Langs = ['Ru', 'En']
Lang = "Ru"
Outputs = ['.txt', 'message']
Output = ['.txt']
Credits = "Bot created by Arcane Dev team and EvolveAI"
lightspeed = 300000000
lightspedt = 299792458
CHAD_API_KEY = os.getenv('CHAD_API_KEY')

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, '''
    Я - бот помощник молодого физика, созданный для Sk challenge.
    Напиши /help для ознакомления со способностями.
    ''')

@bot.message_handler(commands=['wave'])
def waveD(message):
    try:
        arg = message.text.split()[1]
        int_value = int(arg)
        response = bot.send_message(message.chat.id, f'Вы передали значение: {int_value}')
        Wave_script(message, int_value)
    except (IndexError, ValueError):
        bot.send_message(message.chat.id, 'Ошибка! Попробуйте заново ввести промт!')

@bot.message_handler(commands=['flaser'])
def flaser(message):
    Flaser_script(message)

@bot.message_handler(commands=['AI'])
def ai(message):
    AI(message)

def Wave_script(message, wave):
    if "/exc" in message.text:
        cnvrt = lightspedt / wave
    else:
        cnvrt = lightspeed / wave
    m = 1000000
    mhz = cnvrt / m
    bot.send_message(message.chat.id, f'Частота волны равна {round(cnvrt, 1)} Гц или {round(mhz, 1)} Мгц')

def power_to_fluence(power, area, time):
    return power / (area * time)

def Flaser_script(message,chat):
    try:
        args = message.text.split()
        power = float(args[1])
        bot.send_message(chat.id , 'Напишите площадь (см2)')
        try:
             area = int(message.text)
             bot.send_message(chat.id, f'Вы передали значение {area}cm2')
        except IndexError:
             bot.send_message(chat.id, 'Ошибка! Попробуйте изменить промт!')
        bot.send_message(chat.id, 'Теперь отправьте время sec!')
        try:
            time = int(message.text)
            bot.send_message(chat.id, f'Вы передали значение {time}sec')
        except IndexError:
            bot.send_message(chat.id, 'Ошибка! Попробуйте изменить промт!')

        fluence = power_to_fluence(power, area, time)
        bot.reply_to(message, f'Флюенс: {fluence} Дж/см²')
    except (IndexError, ValueError):
        bot.reply_to(message, 'Ошибка! Попробуйте заново ввести промт!')

def WaveRev(message):
    try:
        arg = message.text.split()[1]
        value = float(arg)
        response = bot.send_message(message.chat.id, f'Вы передали значение: {value}')

        if "/exc" in message.text:
            revv = lightspedt * value
        else:
            revv = lightspeed * value

        ms = 3.6
        kmh = revv * ms
        bot.send_message(message.chat.id, f'Скорость фотона = {round(revv, 1)} М/с или {round(kmh, 1)} км/ч')
    except (IndexError, ValueError):
        bot.send_message(message.chat.id, 'Ошибка! Попробуйте заново ввести промт!')

def fluenseRev(message):
    if "/Rev" in message.text and "/flaser" in message.text:
        try:
            args = message.text.split()
            fluence = float(args[1])
            time = 1  # Second
            fl = 1  # Cm2
            power = fluence * fl * time
            bot.reply_to(message, f'Мощность лазера за 1 секунду на 1 кв. см: {power} Вт')
        except (IndexError, ValueError):
            bot.reply_to(message, 'Ошибка! Попробуйте заново ввести промт!')

def CheightR(message):
    bot.send_message(message.chat.id, 'Чтобы вызвать /Cheight отправьте файл "spectrum.txt", и вызовите /Cheight в этом же сообщении')

def Cheight(file_path, message):
    try:
        data = np.loadtxt(file_path)
        x = data[:, 0]
        y = data[:, 1]

        peaks, _ = find_peaks(y)
        peak_x = x[peaks]
        peak_y = y[peaks]

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label='Спектр')
        plt.xlabel('Длина волны')
        plt.ylabel('Интенсивность')
        plt.title('Спектр с отмеченными пиками и шириной на полувысоте')

        for i in range(len(peaks)):
            half_max = peak_y[i] / 2
            left_index = np.where(y[:peaks[i]] <= half_max)[0][-1]
            right_index = np.where(y[peaks[i]:] <= half_max)[0][0] + peaks[i]
            width = x[right_index] - x[left_index]

            bot.send_message(message.chat.id, f'Пик в {peak_x[i]:.3f} с шириной на полувысоте {width:.2f}')
            plt.plot(peak_x[i], peak_y[i], "x", label='Пик', color='red')
            plt.hlines(half_max, x[left_index], x[right_index], color='C3', linestyle='--', label='Полувысота')

        plt.legend()
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(1)
        plt.close()
        bot.send_photo(message.chat.id, buf)
    except Exception as e:
        bot.send_message(message.chat.id, 'Произошла ошибка при обработке файла спектра.')

@bot.message_handler(commands=['constants'])
def send_constants(message):
    try:
        with open('PhysConsts.json', 'r') as f:
            PhysConsts = json.load(f)

        response = "Физические константы:\n"
        for name, data in PhysConsts.items():
            response += f"{name.replace('_', ' ').capitalize()}: {data['value']} {data['unit']}\n"

        bot.send_message(message.chat.id, response)
    except FileNotFoundError:
        bot.send_message(message.chat.id, 'Файл с физическими константами не найден.')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '''
     /wave - вычисление частоты волны
     /Rwave - обратное использование /wave
     /flaser - вычисление флюенса лазера (по умолчанию 1см2, 1сек. В следующем обновлении будет изменяемо)
     /Rflaser - обратное использование /flaser
     /lang - выбор языка
     /credits - информация о создателях
     /settings - настройки
     /AI - ChatGPT 4o
     /PreSets - выбор пресетов
     /Constants - Выводит некоторые физические константы
     /Aistat - посмотреть статистику ии
     Чтобы все было правильно вводите все данные в СИ!
     /cheight - spectrum.txt (синтаксис на GitHub) Вычисление пика и его ширины в полувысоте (График и текст)
     /CheightR - обратный cheight
     /Cheight help - помощь по /Cheight
     /rate -  Оценить работу бота
     /rating - Последние пять отзывов
     Флаги /Rev и /Exc отменены и переработаны в команды! Первое время будут /CheightR /Rflaser и /Rwave ,но позже в пресетах с помощью кнопки можно будет выбрать их без текстовых команд.
     Остальное на GitHub - https://GitHub.com/Nam4ik/SkPhys/tree/master
    ''')

@bot.message_handler(commands=['credits'])
def credits(message):
    bot.send_message(message.chat.id, "Создано командой Arcane Dev team и EvolveAI, @ArcaneDevStudio , @Evolve_AI. Для детей из Skchallenge. Контакт - @Nam4iks")

def AI(message):
    request_json = {
        "message": "Как думаешь, сколько будет 2+9?",
        "api_key": CHAD_API_KEY
    }

    if "/AI" in message.text:
        response = requests.post(url='https://ask.chadgpt.ru/api/public/gpt-4o-mini', json=request_json)
        if response.status_code != 200:
            bot.send_message(message.chat.id, f'Ошибка! Код http-ответа: {response.status_code}')
        else:
            resp_json = response.json()
            if resp_json['is_success']:
                resp_msg = resp_json['response']
                used_words = resp_json['used_words_count']
                bot.reply_to(message, f'Ответ от бота: {resp_msg}\nПотрачено слов: {used_words}')
            else:
                error = resp_json['error_message']
                bot.reply_to(message.chat.id, f'Ошибка: {error}')

#
def rate_step(message, chat):
        index = 0
        bot.send_message(chat.id, 'Введите вашу оценку. От 1 до 10')
        try:
            ratel = message.text.split()
            rates = [value for value in ratel if isinstance(value, int)]
            rate = int(rates)
            print(type(rate))
            if rate < 1 or rate > 10:
                raise ValueError
        except ValueError:
            index += 1
            bot.send_message(message.chat.id, "Спасибо за оценку!")
        ratel = message.text.split()
        rates = [value for value in ratel if isinstance(value, int)]
        rate = int(rate)
        allrates = [None]
        allrates.insert(index, rate)
        with open('rates.json', 'w') as f:
            json.dump(allrates, f)
        with open('rates.json', 'r') as f:
            allrates = json.load(f)
        int_values = [item for item in allrates if isinstance(item, int)]
        str_values = [item for item in allrates if isinstance(item, str)]
        rate = sum(int_values) / len(int_values)
        irate = str_values[-5:]
        bot.send_message(chat.id, f'Последние 5 текстовых отзывов {irate}')
        bot.send_message(chat.id, f'Средняя оценка: {rate}')
        bot.send_message(chat.id, 'Оставьте текстовый отзыв. Если не хотите напишите pass')

        if message.text == 'pass':
            bot.send_message(chat.id, 'Спасибо за оценку!')



def last_rates(message, allratesr, chat):
    int_values = [item for item in allratesr if isinstance(item, int)]
    str_values = [item for item in allratesr if isinstance(item, str)]
    irate = str_values[-5:]
    irateint = int_values[-5:]
    bot.send_message(chat.id, f'''
    Последние несколько отзывов. Текстовые: {irate}
    Числовой рейтинг: {irateint}''')

@bot.message_handler(commands=['rating'])
def callrating(message):
    last_rates(message, allratesr, message.chat)

@bot.message_handler(commands=['rate'])
def callratings(message):
    rate_step(message, message.chat)

@bot.message_handler(commands=['settings'])
def settings(message):
    pass

@bot.message_handler(commands=['AI'])
def callAI(message):
    AI(message)

@bot.message_handler(commands=['Rwave'])
def revW(message):
    WaveRev(message)

@bot.message_handler(commands=['Rflaser'])
def CallFlRev(message):
    fluenseRev(message)

@bot.message_handler(commands=['wave'])
def CallWave(message):
    waveD(message)

@bot.message_handler(commands=['flaser'])
def callFlaser(message):
    Flaser_script(message)

@bot.message_handler(commands=['CheightR'])
def callCheightr(message):
    CheightR(message)

@bot.message_handler(commands=['Cheight help'])
def helpCheight(message):
    CheightR(message)

@bot.message_handler(commands=['Cheight'])
def callCheight(message):
    if 'spectrum.txt' in message.text:
        Cheight('spectrum.txt', message)
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, отправьте файл "spectrum.txt".')

bot.polling()
