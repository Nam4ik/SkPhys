import telebot
import numpy
import math
import requests
from openai import OpenAI
API_TOKEN = '<No_API>'
bot = TeleBot.(N-API)
Langs = ['Ru', 'En']
Lang = "Ru"
Outputs = ['.txt', 'message']
Output = ['.txt']
AIs = ['GPT3.5t', 'GPT4m']
Credits = "Bot created by Arcane Dev team and EvolveAI"
Set = [Lang,Output,AI]

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
def txt_cnvrt(self):
    None
def Wave_script(self):
    None
def Flaser_script(self):
    None
def AI():
    None
def Settings():
    None
def Output():
    None