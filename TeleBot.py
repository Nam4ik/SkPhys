import telebot
import numpy as np
from scipy.signal import find_peaks
import math
import requests
import telebot
from typing import Text
import os
import json
import matplotlib.pyplot as plt
import io
flags=['/rev','/exc']
API_TOKEN=os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)
Langs = ['Ru', 'En']
Lang = "Ru"
Outputs = ['.txt', 'message']
Output = ['.txt']
Credits = "Bot created by Arcane Dev team and EvolveAI"
Set = [Lang,Output]
lightspeed=300000000
lightspedt=299792458
CHAD_API_KEY = os.getenv('CHAD_API_KEY')

@bot.message_handler(commands=['help', 'start', 'wave', 'flaser' ,'Cheight', 'lang', 'credits', 'settings', 'AI', 'PreSets', 'AIstat'])
def welcome(message):
    bot.reply_to(message, '''
    Я - бот помощник молодого физика cозданный для Sk challenge. 
    Напиши /help для ознакомления со способностями. 
    ''')
def Waved(message, chat):
    if "/wave" or "/Wave" in message:
      try:
        arg = message.text.split()[1]  
        int_value = int(arg)  
        response = bot.send_message(f'Вы передали значение: {int_value}')
      except (IndexError, ValueError):
        response = bot.send_message('Пожалуйста, введите команду в формате: /wave <int>')
    bot.polling()
    wave=int_value

def Wave_script(message, wave, chat):
    if "/exc" or "/Exc" in message:
      cnvrt = lightspedt / wave 
    else:
      cnvrt = lightspeed / wave
    m = 1000000
    mhz = cnvrt / m
    bot.send_message(chat.id, f'Частота волны равна {round(cnvrt, 1)} Гц или {round(mhz, 1)} Мгц')

def power_to_fluence(power, area, time):
    return power / (area * time)

def Flaser_script(self, message):
    try:
        args = message.text.split()
        power = float(args[1])  
        area = 1.0  
        time = 1.0 
        
        fluence = power_to_fluence(power, area, time)
        bot.reply_to(message, f'Флюенс: {fluence} Дж/см²')
    except (IndexError):
        bot.reply_to(message, 'Пожалуйста, укажите мощность!')
    except (ValueError):
        bot.reply_to(message, 'Пожалуйста, введите корректное число!')

bot.polling()

    
class Flags():
   def WaveRev(message, chat, self):
    if "/Rev" or "/rev" and "/wave" or "/Wave" in message:
      try:
        arg = message.text.split()[1]  
        value = int(arg) or float(arg) 
        response = bot.send_message(f'Вы передали значение: {value}')
      except (IndexError, ValueError):
        response = bot.send_message('Что-то пошло не так ,попробуйте снова и проверьте команду на наличие ошибок')
      if "/exc" or "/Exc" in message:
         revv = lightspedt * value
         ms = 3.6
         kmh = revv*ms,
         bot.send_message(chat.id f'Скорость фотона = {round(revv, 3)}М/с или {round(kmh, 3)}км/ч')
      else: 
         revv = lightspeed * value
         ms = 3.6
         kmh = revv*ms,
         bot.send_message(chat.id f'Скорость фотона = {round(revv, 1)}М/с или {round(kmh, 1)}км/ч')
         
   def fluenseRev(chat, message, self):
       if "/Rev" or "/rev" and "/flaser" or "/Flaser" in message:
        try:
         args = message.text.split()
         fluence = float(args[1])  or int(args[1])
         time = 1 #Second
         fl = 1 #Cm2
         power = fluence * fl * time
         bot.reply_to(message, f'Мощность лазера за 1 секунду на 1кв. см: {power} Вт')
        except (IndexError):
         bot.reply_to(message, 'Пожалуйста, укажите мощность!')
        except (ValueError):
         bot.reply_to(message, 'Пожалуйста, введите корректное число!')
        if "/Exc" or "/exc" and "/flaser" or "/Flaser" in message:
           IndexError 
       else:
          pass
def CheightR(message, x, y, chat):
# if '/Cheight' or '/cheight' in message:
#   try:
#       arg = message.text.split()[1]
#       arg1= message.text.split(",")[2]
#       x = float.arg1 or int.arg1
#       y = float.arg1[2] or int.arg1[2] 
#   except (IndexError, ValueError):
#       response = bot.send_message(chat.id'Пожалуйста, введите команду в формате: /Cheight <int>/<float>, <int>/<float>/. float - Обязательно через "." к примеру 1.546')
   bot.send_message(chat.id, 'Чтобы вызвать /Cheight отправьте файл "spectum.txt", и вызовите /Cheight в этом же сообщении')
   bot.polling()
   Cheight('spectrum.txt', message, chat)
       


def Cheight(file_path, message, chat):
    
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
        left_index = np.where(y[:peaks[i]] <= half_max)[0][-1]  # Индекс левой границы
        right_index = np.where(y[peaks[i]:] <= half_max)[0][0] + peaks[i]  # Индекс правой границы
        width = x[right_index] - x[left_index]  # Ширина на полувысоте

      
        reply = bot.send_message(chat.id, f'Пик в {peak_x[i]:.2f} с шириной на полувысоте {width:.2f}')

        
        plt.plot(peak_x[i], peak_y[i], "x", label='Пик', color='red')
        plt.hlines(half_max, x[left_index], x[right_index], color='C2', linestyle='--', label='Полувысота')

    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()  
    bot.send_photo(message.chat.id, buf)
    bot.polling()



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

def help(message, chat):

    if '/help' in message:
        bot.send_message(chat.id, '''
     /wave - вычисление частоты волны
      /flaser - вычисление энергии лазера
      /lang - выбор языка
      /credits - информация о создателях
      /settings - настройки
      /AI - выбор AI
      /PreSets - выбор пресетов 
      /Const - Выводит некоторые физические константы 
      /Aistat - посмотреть статистику ии
      Чтобы все было правильно вводите все данные в СИ!
      /cheight - spectrum.txt
      ''')

def credits(message, chat):
    if '/credits' in message and Lang == "Ru":
        bot.send_message(chat.id, "Created by Arcane Dev team and EvolveAI, @ArcaneDevStudio , @Evolve_AI. For Skchallenge kids. Contact me - @Nam4iks")
    if '/credits' in message and Lang == "En":
        bot.send_message(chat.id, "Создано командой Arcane Dev team и EvolveAI, @ArcaneDevStudio , @Evolve_AI. Для детей из Skchallenge. Контакт - @Nam4iks")

def Presets():
    None
def AI(message, self, chat):
  request_json = {
    "message": "Как думаешь, сколько будет 2+9?",
    "api_key": json.load("api_key") or os.getenv("CHAD_API_KEY")}

  if "/AI" or "/ai" in message:
   response = requests.post(url='https://ask.chadgpt.ru/api/public/gpt-4o-mini',
                         json=request_json)
   bot.send_message(chat.id, response)


  if response.status_code != 200:
    print(f'Ошибка! Код http-ответа: {response.status_code}')
    bot.message_send(chat.id, f'Ошибка! Код http-ответа: {response.status_code}')   
  else:

     resp_json = response.json()


     if resp_json['is_success'] and "/Aistat" or "/AIStat" or "/AiStat" or "/aistat" in message:
        resp_msg = resp_json['response']
        used_words = resp_json['used_words_count']
        bot.reply_to(message, f'Ответ от бота: {resp_msg}\nПотрачено слов: {used_words}')
     else:
        error = resp_json['error_message']
        bot.reply_to(message, f'Ошибка: {error}')




def Settings():
    None


def Output():
    None
#Мы ничего не успели!
