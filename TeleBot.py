import telebot
import scipy
import math
import requests
from telebot import types
from typing import Text
from openai import OpenAI
import os
API_TOKEN = '<No_API>'
bot = TeleBot.(N-API)
Langs = ['Ru', 'En']
Lang = "Ru"
Outputs = ['.txt', 'message']
Output = ['.txt']
AIs = ['GPT3.5t', 'GPT4m']
Credits = "Bot created by Arcane Dev team and EvolveAI"
Set = [Lang,Output,AI]
lightspeed=300000000
lightspedt=299792458
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Ты - помощник юного физика и должен отвечать на его возможно глупые вопросы, будь терпелив и отвечай в научном стиле",
        }
    ],
    model="gpt-3.5-turbo",
)
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
    if '/help' in message:
        None


def Flaser_script(self):
    None


def AI():
    None


def Settings():
    None


def Output():
    None