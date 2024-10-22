import telebot
import scipy
import math
import requests
from docutils.nodes import SkipNode
from telebot import types
from typing import Text
import os
API_TOKEN = '<7851183070:AAFqfoPQ5TXY_5oxeboVR532bkpNLvfUinA>'
bot = TeleBot.(API_TOKEN)
Langs = ['Ru', 'En']
Lang = "Ru"
Outputs = ['.txt', 'message']
Output = ['.txt']
AIs = ['GPT3.5t', 'GPT4m']
Credits = "Bot created by Arcane Dev team and EvolveAI"
Set = [Lang,Output,AI]
lightspeed=300000000
lightspedt=299792458
CHAD_API_KEY = 'chad-fa038d409ca54bc0902da28906aa31bafv3tbkoy'



@bot.message_handler(commands=['help', 'start', 'wave', 'flaser' ,'Cheight', 'lang', 'credits', 'settings', 'AI', 'PreSets'])
   def welcome(message):
    bot.reply_to(message, '''
    Я - бот помощник молодого физика cозданный для Sk challenge. 
    Напиши /help для ознакомления со способностями. 
    ''')
def Wave_script(message):
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

def Cheight():
    None


def Lang():
    None


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
      ''')

def credits(message):
    if '/credits' in message and Lang == "En"
        bot.send_message(chat.id, "Created by Arcane Dev team and EvolveAI, @ArcaneDevStudio , @Evolve_AI. For Skchallenge kids. Contact me - @Nam4iks")
    if '/credits' in message and Lang == "En":
        bot.send_message(chat.id, "Создано командой Arcane Dev team и EvolveAI, @ArcaneDevStudio , @Evolve_AI. Для детей из Skchallenge. Контакт - @Nam4iks")

def Presets():
    None

def Flaser_script(self):
    None


def AI():
# Формируем запрос
request_json = {
    "message": "Как думаешь, сколько будет 2+9?",
    "api_key": CHAD_API_KEY
}

# Отправляем запрос и дожидаемся ответа
response = requests.post(url='https://ask.chadgpt.ru/api/public/gpt-4o-mini',
                         json=request_json)

# Проверяем, отправился ли запрос
if response.status_code != 200:
    print(f'Ошибка! Код http-ответа: {response.status_code}')
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