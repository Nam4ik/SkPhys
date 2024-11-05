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
        response = bot.send_message(message.chat.id, 'Пожалуйста, введите команду в формате: /wave <int>') 

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

def Flaser_script(message):
    try:
        args = message.text.split(",")
        power = float(args[1])  
        area = int(args[2])
        time = int(args[3])
        
        fluence = power_to_fluence(power, area, time)
        bot.reply_to(message, f'Флюенс: {fluence} Дж/см²')
    except (IndexError):
        bot.reply_to(message, 'Пожалуйста, укажите мощность!')
    except (ValueError):
        bot.reply_to(message, 'Пожалуйста, введите корректное число!')

def WaveRev(message):
    try:
        arg = message.text.split()[1]  
        value = float(arg) 
        response = bot.send_message(message.chat.id, f'Вы передали значение: {value}')
    except (IndexError, ValueError):
        response = bot.send_message(message.chat.id, 'Что-то пошло не так, попробуйте снова и проверьте команду на наличие ошибок')
    
    if "/exc" in message.text:
        revv = lightspedt * value
    else: 
        revv = lightspeed * value
    
    ms = 3.6
    kmh = revv * ms
    bot.send_message(message.chat.id, f'Скорость фотона = {round(revv, 1)} М/с или {round(kmh, 1)} км/ч')

def fluenseRev(message):
    if "/Rev" in message.text and "/flaser" in message.text:
        try:
            args = message.text.split()
            fluence = float(args[1])
            time = 1  # Second
            fl = 1  # Cm2
            power = fluence * fl * time
            bot.reply_to(message, f'Мощность лазера за 1 секунду на 1 кв. см: {power} Вт')
        except (IndexError):
            bot.reply_to(message, 'Пожалуйста, укажите мощность!')
        except (ValueError):
            bot.reply_to(message, 'Пожалуйста, введите корректное число!')

@bot.message_handler(commands=['Cheight'])
def CheightR(message):
    bot.send_message(message.chat.id, 'Чтобы вызвать /Cheight отправьте файл "spectrum.txt", и вызовите /Cheight в этом же сообщении')

def Cheight(file_path, message):
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

        bot.send_message(message.chat.id, f'Пик в {peak_x[i]:.2f} с шириной на полувысоте {width:.2f}')
        plt.plot(peak_x[i], peak_y[i], "x", label='Пик', color='red')
        plt.hlines(half_max, x[left_index], x[right_index], color='C2', linestyle='--', label='Полувысота')

    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()  
    bot.send_photo(message.chat.id, buf)

@bot.message_handler(commands=['constants'])
def send_constants(message):
    with open('PhysConsts.json', 'r') as f:
        PhysConsts = json.load(f)
    
    response = "Физические константы:\n"
    for name, data in PhysConsts.items():
        response += f"{name.replace('_', ' ').capitalize()}: {data['value']} {data['unit']}\n"
    
    bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '''
     /wave - вычисление частоты волны `/wave <int>`
     /flaser - вычисление энергии лазера `/wave <int>(power), <int>(area cm2), <int>(time - sec)`
     /lang - выбор языка - in dev
     /credits - информация о создателях
     /settings - настройки - in dev
     /AI - ответ ChatGPT
     /PreSets - выбор пресетов - in dev 
     /Constants - Выводит некоторые физические константы 
     /Aistat - посмотреть статистику ии
     Чтобы все было правильно вводите все данные в СИ!
     Флаги
     /Rev , /Exc 
     /Exc - Точно - Выводит более точное значение
     /Rev - Использование команды наоборот
     
     /cheight - spectrum.txt - вычисление пика и его ширины в полувысоте
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
                bot.reply_to(message, f'Ошибка: {error}'

@bot.message_handler(commands=['wave'])
if "/rev" in message.text or "/Rev" in message.text:
    WaveRev(message)
else:
    WaveD(message)
    Wave_script(message)
@bot.message_handler(commands=['flaser'])
if "/rev" in message.text or "/Rev" in message.text:
    fluenseRev(message)
else:
    fluense(message)
    fluense_script(message)
@bot.message_handler(commands=['Cheight'])
if "/rev" in message.text or "/Rev" in message.text:
    CheightR(message)
else:
    Cheight(message)
@bot.message_handler(commands=['AI'])
bot.polling()
