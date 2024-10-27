import telebot
import numpy as np
from scipy.signal import find_peaks
import math
import requests
import telebot
from typing import Text
import os
from translate import Translator
import json
API_TOKEN=os.getenv('API_TOKEN')
bot = teleBot.bot(API_TOKEN)
Langs = ['Ru', 'En']
Lang = "Ru"
Outputs = ['.txt', 'message']
Output = ['.txt']
AIs = ['GPT3.5t', 'GPT4m']
Credits = "Bot created by Arcane Dev team and EvolveAI"
Set = [Lang,Output,AIs]
lightspeed=300000000
lightspedt=299792458
CHAD_API_KEY = os.getenv('CHAD_API_KEY')
@bot.message_handler(commands=['help', 'start', 'wave', 'flaser' ,'Cheight', 'lang', 'credits', 'settings', 'AI', 'PreSets'])
def welcome(message):
    bot.reply_to(message, '''
    Я - бот помощник молодого физика cозданный для Sk challenge. 
    Напиши /help для ознакомления со способностями. 
    ''')
def wavei(message, self, wave):
 if "/wave" or "/Wave" in message:
   try:
             
        arg = message.text.split()[1]  
        int_value = int(arg)  
        response = f'Вы передали значение: {int_value}'
   except (IndexError, ValueError):
        response = 'Пожалуйста, введите команду в формате: /wave <int>'
   wave=int_value
   bot.polling()

def Wave_script(message, wave):
    cnvrt = lightspeed / wave
    m = 1000000
    mhz = cnvrt / m
    bot.send_message(chat.id, f'Частота волны равна {round(cnvrt, 1)} Гц или {round(mhz, 1)} Мгц')


def txt_cnvrt(self, message):
    if '/wave' in message:
      with open('output.txt', 'w') as f:
       f.write(Wave_script())
       bot.reply_to(message)
       bot.send_message(chat.id, f)
       bot.polling()

def CheightR(Cheight, message, x, y):
 if '/Cheight' or '/cheight' in message:
   try:
       arg = message.text.split()[1]
       arg1= message.text.split(",")[2]
       x = float.arg1 or int.arg1
       y = float.arg1[2] or int.arg1[2] 
   except (IndexError, ValueError):
        response = 'Пожалуйста, введите команду в формате: /Cheight <int>/<float>, <int>/<float> (float - Обязательно через "." к примеру 1.546)'
   bot.polling()
      
       


def Cheight(x, y):
    peaks, _ = find_peaks(y)
peak_x = x[peaks]
peak_y = y[peaks]

for i in range(len(peaks)):
    half_max = peak_y[i] / 2
    left_index = np.where(y[:peaks[i]] <= half_max)[0][-1]
    right_index = np.where(y[peaks[i]:] <= half_max)[0][0] + peaks[i]
    width = x[right_index] - x[left_index]
    
    reply= bot.send_message(chat.id, f'Пик в {peak_x[i]:.2f} с шириной на полувысоте {width:.2f}')


def Lang():
    None

def consts(self, message):
    with open('PhysConsts.json', 'r') as f:
     PhysConsts = json.load(f)

@bot.message_handler(commands=['constants'])
def send_constants(message):
    response = "Физические константы:\n"
    for name, data in consts.items():
        response += f"{name.replace('_', ' ').capitalize()}: {data['value']} {data['unit']}\n"
    
    bot.send_message(message.chat.id, response)

bot.polling()

def help(message):

    if '/help' in message:
        bot.send_message(chat.id, '''
     /wave - вычисление частоты волны
      /flaser - вычисление энергии лазера
      /lang - выбор языка
      /credits - информация о создателях
      /settings - настройки
      /AI - выбор AI
      /PreSets - выбор пресетов 
      /Cheight - 
      /Const - Выводит некоторые физические константы 
      Чтобы все было правильно вводите все данные в СИ!
      ''')

def credits(message):
    if '/credits' in message and Lang == "Ru":
        bot.send_message(chat.id, "Created by Arcane Dev team and EvolveAI, @ArcaneDevStudio , @Evolve_AI. For Skchallenge kids. Contact me - @Nam4iks")
    if '/credits' in message and Lang == "En":
        bot.send_message(chat.id, "Создано командой Arcane Dev team и EvolveAI, @ArcaneDevStudio , @Evolve_AI. Для детей из Skchallenge. Контакт - @Nam4iks")

def Presets():
    None
def power_to_fluence(power, area, time):
    return power / (area * time)

def Flaser_script(self):
     try:
        # Извлечение аргументов
        args = message.text.split()
        power = float(args[1])  # Мощность лазера
        area = 1.0  # Например, 1 см² (можно поменять по нужде)
        time = 1.0  # Например, 1 секунда (можно поменять по нужде)
        
        fluence = power_to_fluence(power, area, time)
        bot.reply_to(message, f'Флюенс: {fluence} Дж/см²')
    except (IndexError):
        bot.reply_to(message, 'Пожалуйста, укажите мощность!')
    except (ValueError):
        bot.reply_to(message, 'Пожалуйста, введите корректное число!')

bot.polling()

    
def AI(message, self):
  request_json = {
    "message": "Как думаешь, сколько будет 2+9?",
    "api_key": CHAD_API_KEY}

# Отправляем запрос и дожидаемся ответа
  response = requests.post(url='https://ask.chadgpt.ru/api/public/gpt-4o-mini',
                         json=request_json)
  telebot.bot(chat.id, send_message )

# Проверяем, отправился ли запрос
  if response.status_code != 200:
    print(f'Ошибка! Код http-ответа: {response.status_code}')
    bot.message_send(chat.id, f'Ошибка! Код http-ответа: {response.status_code}')   
  else:
    # Получаем текст ответа и преобразовываем в dict
     resp_json = response.json()

    # Если успешен ответ, то выводим
     if resp_json['is_success']:
        resp_msg = resp_json['response']
        used_words = resp_json['used_words_count']
        print(f'Ответ от бота: {resp_msg}\nПотрачено слов: {used_words}')
     else:
        error = resp_json['error_message']
        print(f'Ошибка: {error}')




def Settings():
    None


def Output():
    None