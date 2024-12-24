#                MIT License
#
#                Copyright (c) 2024 ArcaneDev
#
#                Permission is hereby granted, free of charge, to any person obtaining a copy
#                of this software and associated documentation files (the "Software"), to deal
#                in the Software without restriction, including without limitation the rights
#                to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#                copies of the Software, and to permit persons to whom the Software is
#                furnished to do so, subject to the following conditions:
#
#                The above copyright notice and this permission notice shall be included in all
#                copies or substantial portions of the Software.
#
#                THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#                IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#                FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#                AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#                LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#                OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#                BUT YOU CAN'T TOUCH, USING AND SEEING API KEYS AND OTHER NOT FREE PROJECT PARTS  
#                YOU SHOULDNT MAKE A LOSS TO THE AUTHOR AND DEVELOPERS TEAM 


#                 ____  _    ____  _                 _           _     _           
#                / ___|| | _|  _ \| |__  _   _ ___  | |__   ___ | |_  | |__  _   _ 
#                \___ \| |/ / |_) | '_ \| | | / __| | '_ \ / _ \| __| | '_ \| | | |
#                 ___) |   <|  __/| | | | |_| \__ \ | |_) | (_) | |_  | |_) | |_| |
#                |____/|_|\_\_|   |_| |_|\__, |___/ |_.__/ \___/ \__| |_.__/ \__, |
#                    _                   |___/     ____                 _____|___/ 
#                   / \   _ __ ___ __ _ _ __   ___|  _ \  _____   __   / ___ \     
#                  / _ \ | '__/ __/ _` | '_ \ / _ \ | | |/ _ \ \ / /  / | _ \ \    
#                 / ___ \| | | (_| (_| | | | |  __/ |_| |  __/\ V /  |  |   /  |   
#                /_/   \_\_|  \___\__,_|_| |_|\___|____/ \___| \_/    \ |_|_\ /    
#                                                                      \_____/     


#import os
#import fuel
import telebot
from telebot import types
import numpy as np
from scipy.signal import find_peaks
import requests
import pandas as pd 
import json
import matplotlib.pyplot as plt
import io
import api
import logging



logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
#flags = ['/rev', '/exc']
bot = telebot.TeleBot(api.API_TOKEN)
#Langs = ['Ru', 'En']
#Lang = "Ru"
#Outputs = ['.txt', 'message']
#Output = ['.txt']
Credits = "Bot created by Arcane Dev team and EvolveAI"
lightspeed = 300000000
lightspedt = 299792458
CHAD_API_KEY = api.CHAD_API_KEY
markup =types.ReplyKeyboardMarkup(resize_keyboard=True)
exit =  types.KeyboardButton('Назад')
func =  types.KeyboardButton('Функции')
fcredit=types.KeyboardButton('О создателях')
reply=  types.KeyboardButton('Связаться с нами')
btn  =  types.KeyboardButton('Настройки')
btn0 =  types.KeyboardButton('ИИ')
btn1 =  types.KeyboardButton('Помощь')
btn2 =  types.KeyboardButton('Оценки')
btn3 =  types.KeyboardButton('Посмотреть оценки')
btn4 =  types.KeyboardButton('Флюенс лазерной системы')
btn5 =  types.KeyboardButton('Мощность лазерной системы')
btn6 =  types.KeyboardButton('Пик и его ширина в полувысоте')
btn7 =  types.KeyboardButton('Частота излучения в длину волны')
btn8 =  types.KeyboardButton('Длина волны в частоту')
btnn =  types.KeyboardButton('Колебательный контур')
fuelv=  types.KeyboardButton('Виды отопления и их цена')
contr=  types.KeyboardButton('Рассчет колебательного контура')
prices       = None 
FUEL_PRICE   = None 
usd_rate     = None
eur_rate     = None
your_squares = int 
#def load_price(message):
#    try:
#        prices = message.text.split(',')
#        if len(prices) != 3:
#            bot.send_message(message.chat.id, "Неверный формат данных. Пожалуйста, введите три значения через запятую.")
#        bot.register_next_step_handler(your_squere, choosing_a_heating_source)
#    except:
#        bot.send_message(message.chat.id, "Неверный формат данных. Пожалуйста, введите три значения через запятую.")

def load_price(message):
    # Объявляем, что мы будем использовать глобальную переменную
    try:
        prices = message.text.split(',')
        if len(prices) != 3:
            bot.send_message(message.chat.id, "Неверный формат данных. Пожалуйста, введите три значения через запятую.")
            return
        FUEL_PRICE = list(map(float, prices))  # Преобразуем строки в числа
        bot.register_next_step_handler(message, choosing_a_heating_source)
    except:
        bot.send_message(message.chat.id, "Неверный формат данных. Пожалуйста, введите три значения через запятую.")

#def valutecources(message, count):
#   get_exchange_rates()
#    PriceInEUR = get_exchange_rates.cource.eur * count 
#    PriceInUSD = get_exchange_rates.cource.usd * count 
def your_sqare(message): 
    try:
     bot.send_message(message.chat.id, "Введите площадь вашего дома/квартиры(m2)")
     bot.register_next_step_handler(message, load_yoursquare)
    except ValueError:
     bot.send_message(message.chat.id, "Неверный формат данных. Пожалуйста, введите число.")
#your_square = (input('Введите площадь вашего дома/квартиры: '))

def load_yoursquare(message):
  try:  
    global your_squares
    yout_squares = int(message.text)
    bot.send_message(message.chat.id, f"Значение пртинято")
    bot.register_next_step_handler(message, choose_fuel)
  except ValueError:
    bot.send_message(message.chat.id, "Неверный формат данных. Пожалуйста, введите число.")

def choose_fuel(message):
    bot.send_message(message.chat.id , "Посмотрите на меню. ")
    global valutes
    global isvalute
    valutes = ['Ruble', 'Euro', 'Dollar']
    isvalute = valutes[0]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    fuel = types.KeyboardButton("Сменить цены на топливо вручную") 
    preset = types.KeyboardButton("Выбрать региональный пресет") 
    nrm = types.KeyboardButton("Меня устраивает")
    markup.add(nrm ,fuel, preset, exit) 
    bot.send_message(message.chat.id, "Настройки", reply_markup=markup)
    @bot.message_handler(func=lambda message: message.text == "Выбрать региональный пресет")
    def regional_prices(message):
        global Russia
        Russia = "Россия"
        with open("valuepresets.json", "r") as presets:
            Presets = json.load(presets)
            bot.send_message(message.chat.id, "Пресет загружен! Учтите то что цены актуальны на момент 18.12.2024")
        try:
            response = "Региональные цены:\n"
            for Russia in Presets.items():
                response += f"{Presets.replase('_', ' ').capitalize()}"
                bot.send_message(message.chat.id ,response)
        except FileNotFoundError:
                bot.send_message(message.chat.id, 'Файл не найден! Администрация скоро устранит это ошибку. Для ускорения событий напишите @Nam4iks')
        except ValueError:
            pass 
        except KeyError:
            pass 
        except AttributeError:
            pass
        except json.JSONDecodeError:
            bot.send_message(message.chat.id, 'Файл не найден! Администрация скоро устранит это ошибку. Для ускорения событий напишите @Nam4iks')
        except Exception as e:
            bot.send_message(message.chat.id, f"Произошла ошибка: {e}")
#                try:
#        with open('PhysConsts.json', 'r') as f:
#            PhysConsts = json.load(f)
#
#        response = "Физические константы:\n"
#        for name, data in PhysConsts.items():
#            response += f"{name.replace('_', ' ').capitalize()}: {data['value']} {data['unit']}\n"
#
#       bot.send_message(message.chat.id, response)
#   except FileNotFoundError:
#        bot.send_message(message.chat.id, 'Файл с физическими константами не найден.')
        bot.send_message(message.chat.id, "Чтобы выбрать пресет напишите название города.")
        bot.register_next_step_handler(message, choose_fuel.find_preset)
        
    def find_matching_key(Presets, search_string):
        matches = []

    # Рекурсивная функция для обхода JSON
        def recursive_search(d):
         if isinstance(d, dict):
                for key, value in d.items():
                    if search_string.lower() in key.lower():  # Сравнение без учета регистра
                        matches.append(key)
                    recursive_search(value)  # Рекурсивный вызов для вложенных структур
         elif isinstance(d, list):
                for item in d:
                 recursive_search(item)

        recursive_search(Presets)
        return matches


        def find_preset(message):
          global FUEL_PRICE 
          FUEL_PRICE = []
          try:
            recursive_search(message.text, d=Presets)
            FUEL_PRICE[0] = дрова 
            FUEL_PRICE[1] = газ_баллон
            FUEL_PRICE[2] = топливо
          except ValueError: 
            pass 
           
    # @bot.message_handler(func=lambda message: message.text == "Меня устраивает")
    # def next():
    #     bot.register_next_step_handler(message ,choosing_a_heating_source)
    # @bot.message_handler(func=lambda message: message.text == "Сменить цены на топливо вручную")
    # def editprices(message):
    #         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #         y = types.KeyboardButton("Да")
    #         n = types.KeyboardButton("Нет")
    #         bot.send_message(message.chat.id, f"Введите три значение через запятую дрова, топливо, газ. (Введете не правильно придеться перезапускать функцию) Валюта = {isvalute}")
    #         markup.add(y, n, exit)
    #         bot.send_message(message.chat.id, "Сменить валюту? [Да/Нет]", reply_markup=markup)
    #         @bot.message_handler(func=lambda message: message.text == "Да")
    #         def editvalute(message):
    #             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #             euro = types.KeyboardButton("Euro")
    #             dollar = types.KeyboardButton("Dollar")
    #             ruble = types.KeyboardButton("Ruble")
    #             markup.add(euro, dollar, ruble, exit)
    #             bot.send_message(message.chat.id, f"Варианты валют - [{valutes}]. Текущая валюта - {isvalute} ")
    #             bot.send_message(message.chat.id, f"Курс евро и доллара {get_exchange_rates()}", reply_markup=markup)
    #             @bot.message_handler(func=lambda message: message.text == f"{int}, {int}, {int}")
    #             def editprices(message):
    #                 values = message.text.split(',')
    #                 FUEL_PRICE[0] = values[0]
    #                 FUEL_PRICE[1] = values[1]
    #                 FUEL_PRICE[2] = values[2]
    #                 bot.send_message(message.chat.id, f"Цены на топливо изменены")
    #                 bot.register_next_step_handler(message, choosing_a_heating_source)
    #             @bot.message_handler(func=lambda message: message.text == "Euro")
    #             def euro(message):
    #                 isvalute = valutes[1]
    #                 bot.send_message(message.chat.id, f"Валюта изменена на {isvalute}")
    #                 bot.send_message(message.chat.id, f"Курс евро и доллара {get_exchange_rates()}")
    #                 bot.register_next_step_handler(message, choosing_a_heating_source)
    #             @bot.message_handler(func=lambda message: message.text == "Dollar")
    #             def dollar(message):
    #                 isvalute = valutes[2]
    #                 bot.send_message(message.chat.id, f"Валюта изменена на {isvalute}")
    #                 bot.send_message(message.chat.id, f"Курс евро и доллара {get_exchange_rates()}")
    #             @bot.message_handler(func=lambda message: message.text == "Ruble")
    #             def ruble(message):
    #                 isvalute = valutes[0]
    #                 bot.send_message(message.chat.id, f"Валюта изменена на {isvalute}")
    #                 bot.send_message(message.chat.id, f"Курс евро и доллара {get_exchange_rates()}")
    #             #TODO - Починить этот логический блок
    #             bot.send_message(message.chat.id, f"Введите три значение через запятую дрова, газ, топливо. Валюта = {isvalute}")
    #             bot.register_next_step_handler(message, load_price)
    #         @bot.message_handler(func=lambda message: message.text == "Нет")
    #         def exitf():
    #             menu(message)

def choose_fuel(message):
    logger.info("Entering choose_fuel function.")
    bot.send_message(message.chat.id, "Посмотрите на меню.")
    
    global valutes
    global isvalute
    valutes = ['Ruble', 'Euro', 'Dollar']
    isvalute = valutes[0]
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    fuel = types.KeyboardButton("Сменить цены на топливо вручную") 
    preset = types.KeyboardButton("Выбрать региональный пресет") 
    nrm = types.KeyboardButton("Меня устраивает")
    markup.add(nrm, fuel, preset, exit) 
    
    bot.send_message(message.chat.id, "Настройки", reply_markup=markup)
    
    @bot.message_handler(func=lambda message: message.text == "Выбрать региональный пресет")
    def regional_prices(message):
        logger.info("User  selected regional prices.")
        global Russia
        Russia = "Россия"
        try:
            with open("valuepresets.json", "r") as presets:
                Presets = json.load(presets)
                bot.send_message(message.chat.id, "Пресет загружен! Учтите то что цены актуальны на момент 18.12.2024")
                
            response = "Региональные цены:\n"
            for key, value in Presets.items():
                response += f"{key.replace('_', ' ').capitalize()}: {value}\n"
            bot.send_message(message.chat.id, response)
        except FileNotFoundError:
            logger.error("File not found: valuepresets.json")
            bot.send_message(message.chat.id, 'Файл не найден! Администрация скоро устранит эту ошибку. Для ускорения событий напишите @Nam4iks')
        except json.JSONDecodeError:
            logger.error("JSON decode error while loading presets.")
            bot.send_message(message.chat.id, 'Ошибка при чтении файла пресетов. Проверьте формат JSON.')
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

    @bot.message_handler(func=lambda message: message.text == "Меня устраивает")
    def next():
        logger.info("User  is satisfied with the current settings.")
        bot.register_next_step_handler(message, choosing_a_heating_source)

    @bot.message_handler(func=lambda message: message.text == "Сменить цены на топливо вручную")
    def editprices(message):
        logger.info("User  wants to edit fuel prices.")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        y = types.KeyboardButton("Да")
        n = types.KeyboardButton("Нет")
        bot.send_message(message.chat.id, f"Введите три значения через запятую дрова, топливо, газ. (Введете не правильно придеться перезапускать функцию) Валюта = {isvalute}")
        markup.add(y, n, exit)
        bot.send_message(message.chat.id, "Сменить валюту? [Да/Нет]", reply_markup=markup)

        @bot.message_handler(func=lambda message: message.text == "Да")
        def editvalute(message):
            logger.info("User  chose to change currency.")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            euro = types.KeyboardButton("Euro")
            dollar = types.KeyboardButton("Dollar")
            ruble = types.KeyboardButton("Ruble")
            markup.add(euro, dollar, ruble, exit)
            bot.send_message(message.chat.id, f"Варианты валют - [{valutes}]. Текущая валюта - {isvalute} ")
            bot.send_message(message.chat.id, f"Курс евро и доллара {get_exchange_rates()}", reply_markup=markup)

            @bot.message_handler(func=lambda message: message.text in valutes)
            def change_currency(message):
                global isvalute
                isvalute = message.text
                logger.info(f"Currency changed to {isvalute}.")
                bot.send_message(message.chat.id, f"Валюта изменена на {isvalute}")
                bot.send_message(message.chat.id, f"Курс евро и доллара {get_exchange_rates()}")
                bot.register_next_step_handler(message, choosing_a_heating_source)

        @bot.message_handler(func=lambda message: message.text == "Нет")
        def exitf():
            logger.info("User  chose not to change prices.")
            menu(message)


def pricesset(message):
 if FUEL_PRICE is None:
    FUEL_PRICE = [8, 42, 27]        
    bot.send_message(message.chat.id, "Установлены базовые значения цен на топливо")

def choosing_a_heating_source(your_squares, message):
    # Энергоэффективность топлива (константы)
    density = [600, 2.019]#(плотность)
    ENERGY_EFFICIENCY = [10.62, 4.66, 7.33]
    # Цена топлива (константы) 
    # Основной расчет

    if FUEL_PRICE[2] >= 1000:
       FUEL_PRICE[2] = FUEL_PRICE[2] / density[0]    
       FUEL_PRICE[1] = FUEL_PRICE[1] / density[1]
       
    output_1 = your_squares * 720 * FUEL_PRICE[0] / ENERGY_EFFICIENCY[0]
    output_2 = your_squares * 720 * FUEL_PRICE[1] / ENERGY_EFFICIENCY[1]
    output_3 = your_squares * 720 * FUEL_PRICE[2] / ENERGY_EFFICIENCY[2]

    if isvalute == 'Dollar':
        output_1 *= usd_rate
        output_2 *= usd_rate
        output_3 *= usd_rate
    elif isvalute == 'Euro':
        output_1 *= eur_rate
        output_2 *= eur_rate
        output_3 *= eur_rate
    bot.register_next_step_handler(message, output_1, output_2, output_3, fuel)
    return output_1, output_2, output_3

  
def get_exchange_rates():
    # URL API для получения курсов валют
    url = "https://open.er-api.com/v6/latest/RUB"
    
    try:
        # Выполняем GET-запрос к API
        response = requests.get(url)
        # Проверяем, был ли запрос успешным
        response.raise_for_status()

        # Парсим JSON-ответ
        data = response.json()

        # Извлекаем курсы евро и доллара
        usd_rate = data['rates']['USD']  # Курс доллара к рублю
        eur_rate = data['rates']['EUR']  # Курс евро к рублю

        return usd_rate, eur_rate
    
    except requests.exceptions.RequestException as e:
        print("Ошибка при запросе данных:", e)
        return None, None
    def cource():
       usd, eur = get_exchange_rates()
       if usd is not None and eur is not None:
           print(f"Курс доллара к рублю: {usd}")
           print(f"Курс евро к рублю: {eur}")
           return usd, eur

#results = choosing_a_heating_source(your_squares, message)

def fuel(message, output_1, output_2, output_3): 
    bot.send_message(message.chat.id, f'Затраты на отопление при использовании:')
    bot.send_message(message.chat.id, f'Газ: {round(output_1, 2)} {isvalute}')
    bot.send_message(message.chat.id, f'Дрова: {round(output_2, 2)} {isvalute}')
    bot.send_message(message.chat.id, f'Газ в баллонах: {round(output_3, 2)} {isvalute}')



#def fuel(message): 
#    bot.send_message(message.chat.id, f'Затраты на отопление при использовании:')
#    bot.send_message(message.chat.id, f'Газ: {round(results[0], 2)} {isvalute}')
#    bot.send_message(message.chat.id, f'Дрова: {round(results[1], 2)} {isvalute}')
#    bot.send_message(message.chat.id, f'Газ в баллонах: {round(results[2], 2)} {isvalute}')

@bot.message_handler(commands=['start'])
def welcome(message):
    markup.add(btn, btn1, btn2, btn3)
    bot.reply_to(message, '''
    Я - бот помощник молодого физика, созданный для Sk challenge.
    Напиши /help для ознакомления со способностями. (Учтите то что бот работает со значениями в основном типа int и СИ системе)

    ‼️Если бот не отвечает то он не сломался! Если бот завис по среди команды то напишите ему абсолютно любой текст (не команду) например "." или просто рандомный текст.
    Как правило это решает проблему. Если это не помогает то напишите нам в бот поддержки - @RawLogicBot или в личные сообщения автороам /credits (лучше боту)
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

def Wave_bot(message):
    bot.send_message(message.chat.id, "Введите длину волны (m)")
    bot.register_next_step_handler(message, Wave_script)
def Wave_script(message):
#    if "/exc" in message.text:
#        cnvrt = lightspedt / wave
#    else:
#        cnvrt = lightspeed / wave
    wave = float(message.text)
    cnvrt = lightspeed / wave
    m = 1000000
    mhz = cnvrt / m
    bot.send_message(message.chat.id, f'Частота волны равна {round(cnvrt, 1)} Гц или {round(mhz, 1)} Мгц')

def power_to_fluence(power, area, time):
    return power / (area * time)

def Flaser_script(message):
    bot.send_message(message.chat.id, "Укажите значение мощности лазерной системы в Wt (int)")
    bot.register_next_step_handler(message, process_power)

def process_power(message):
    try:
        power = float(message.text)  # Извлекаем мощность
        bot.send_message(message.chat.id, 'Напишите площадь (см²)')
        bot.register_next_step_handler(message, process_area, power)
    except ValueError:
        bot.reply_to(message, 'Ошибка! Убедитесь, что мощность указана правильно.')

def process_area(message, power):
    try:
        area = float(message.text)  # Извлекаем площадь
        bot.send_message(message.chat.id, 'Теперь отправьте время (секунды)!')
        bot.register_next_step_handler(message, process_time, power, area)
    except ValueError:
        bot.send_message(message.chat.id, 'Ошибка! Пожалуйста, введите площадь в числовом формате.')

def process_time(message, power, area):
    try:
        time = float(message.text)  # Извлекаем время
        fluence = power_to_fluence(power, area, time)
        bot.reply_to(message, f'Флюенс: {fluence:.2f} Дж/см²')
    except ValueError:
        bot.send_message(message.chat.id, 'Ошибка! Пожалуйста, введите время в числовом формате.')
def WaveRev(message):
    args = message.text.split()
    if len(args) < 2:
        bot.send_message(message.chat.id, 'Ошибка! Необходимо указать значение.')
        return
    
    try:
        value = float(args[1])
        if "/exc" in message.text:
            revv = lightspedt * value
        else:
            revv = lightspeed * value

        ms = 3.6
        kmh = revv * ms
        bot.send_message(message.chat.id, f'Скорость фотона = {round(revv, 1)} М/с или {round(kmh, 1)} км/ч')
    except ValueError:
        bot.send_message(message.chat.id, 'Ошибка! Убедитесь, что значение указано правильно.')


def rate_step(message, chat):
    bot.send_message(chat.id, 'Введите вашу оценку. От 1 до 10')
    bot.register_next_step_handler(message, process_rating)

def process_rating(message):
    try:
        rate = int(message.text)
        if rate < 1 or rate > 10:
            bot.send_message(message.chat.id, "Ошибка! Оценка должна быть от 1 до 10.")
            return

        # Сохранение оценки
        with open('rates.json', 'r') as f:
            allrates = json.load(f)
        
        allrates.append(rate)
        with open('rates.json', 'w') as f:
            json.dump(allrates, f)

        bot.send_message(message.chat.id, 'Спасибо за оценку!')
    except ValueError:
        bot.send_message(message.chat.id, 'Ошибка! Пожалуйста, введите числовую оценку.')

def WaveRev(message, chat):
    try:
        bot.send_message(chat.id, 'Введите длину волны')
        value = float(message.text)
        response = bot.send_message(message.chat.id, f'Вы передали значение: {value}')

#        if "/exc" in message.text:
#            revv = lightspedt * value
#        else:
#            revv = lightspeed * value
        global tought 
        tought = False
        revv = lightspeed * value 
        if tought == True:
            revv = lightspedt * value 
            tought = False 
        else:
            revv = lightspeed * value 
            tought = False
        ms = 3.6
        kmh = revv * ms
        bot.send_message(message.chat.id, f'Скорость фотона = {round(revv, 1)} М/с или {round(kmh, 1)} км/ч')
    except (IndexError, ValueError):
        bot.send_message(message.chat.id, 'Ошибка! Попробуйте заново ввести промт!')

#def FluenseToWt(message):
#    pass 
#def fluenseRev(message):
#     bot.send_message(message.chat.id, "Введите флюенс (Дж/см2)")
#     bot.register_next_step_handler(message, )
#    if "/Rev" in message.text and "/flaser" in message.text:
#        try:
#            args = message.text.split()
#            fluence = float(args[1])
#            time = 1  # Second
#            fl = 1  # Cm2
#            power = fluence * fl * time
#            bot.reply_to(message, f'Мощность лазера за 1 секунду на 1 кв. см: {power} Вт')
#        except (IndexError, ValueError):
#            bot.reply_to(message, 'Ошибка! Попробуйте заново ввести промт!')

def CheightR(message):
    bot.send_message(message.chat.id, 'Чтобы вызвать /Cheight отправьте файл "spectrum.txt", и вызовите /Cheight в этом же сообщении')

#def Cheight(message, chat):
#    with open("spectrum.txt", "r") as spectr:
#        spectr.read()
#        if spectr.read()==True:
#            bot.send_message(chat.id ,"Файл загружен")
#    try:
#        data = np.loadtxt(spectr)
#        x = data[:, 0]
#        y = data[:, 1]
#
#        peaks, _ = find_peaks(y)
#        peak_x = x[peaks]
#        peak_y = y[peaks]
#
#        plt.figure(figsize=(10, 6))
#        plt.plot(x, y, label='Спектр')
#        plt.xlabel('Длина волны')
#        plt.ylabel('Интенсивность')
#        plt.title('Спектр с отмеченными пиками и шириной на полувысоте')
#
#        for i in range(len(peaks)):
#            half_max = peak_y[i] / 2
#            left_index = np.where(y[:peaks[i]] <= half_max)[0][-1]
#            right_index = np.where(y[peaks[i]:] <= half_max)[0][0] + peaks[i]
#            width = x[right_index] - x[left_index]
#
#            bot.send_message(message.chat.id, f'Пик в {peak_x[i]:.3f} с шириной на полувысоте {width:.2f}')
#            plt.plot(peak_x[i], peak_y[i], "x", label='Пик', color='red')
#            plt.hlines(half_max, x[left_index], x[right_index], color='C3', linestyle='--', label='Полувысота')
#
#        plt.legend()
#        buf = io.BytesIO()
#        plt.savefig(buf, format='png')
#        buf.seek(1)
#        plt.close()
#        bot.send_photo(message.chat.id, buf)
#    except Exception as e:
#        bot.send_message(message.chat.id, 'Произошла ошибка при обработке файла спектра. Проверьте правильность синтаксиса на https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html')

def circuitq(message):
    bot.send_message(message.chat.id, "Введите индуктивность катушки")
    bot.register_next_step_handler(message, incircuit)

def incircuit(message):
    try:
        global inductive
        inductive = int(message.text)
        bot.send_message(message.chat.id, "Введите емкость конденсатора")
        bot.register_next_step_handler(message, inemc)  # Передаем только функцию inemc
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка! Error = {e}")
        menu(message)

def inemc(message):
    try:
        global emc  # Объявляем emc как глобальную переменную
        emc = int(message.text)
        bot.send_message(message.chat.id, "Введите время в секундах и мы приступим к рассчетам!")
        bot.register_next_step_handler(message, z)  # Передаем только функцию z
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка! Error = {e}")
        menu(message)

def z(message):
    try:
        time_duration = int(message.text)
        bot.register_next_step_handler(message, oscillatory_circuit, L=inductive, C=emc, time_duration=time_duration)
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка! Error = {e}")
        menu(message)

def oscillatory_circuit(message, L, C, time_duration=2):
    f = 1 / (2 * np.pi * np.sqrt(L * C))

    t = np.linspace(0, time_duration * f, 1000)

    V = np.sin(2 * np.pi * f * t)

    plt.figure(figsize=(10, 5))
    plt.plot(t, V)
    plt.title('Колебательный контур')
    plt.xlabel('Время')
    plt.ylabel('Напряжение')
    plt.grid()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    #plt.savefig("C:\Users\User\Desktop", format=".png")
    buf.seek(0)  # Сшросить указатель в начало буфера
    bot.send_photo(message.chat.id, buf)

def Cheight(message, chat):
    try:
        # Проверка наличия файла
        with open("spectrum.txt", "r") as spectr:
            lines = spectr.readlines()
            if not lines:
                bot.send_message(chat.id, "Файл пуст.")
                return

        # Загрузка данных из файла
        data = np.loadtxt("spectrum.txt")
        x = data[:, 0]
        y = data[:, 1]

        # Поиск пиков
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
        buf.seek(0)
        plt.close()
        buf.name = 'spectrum.png'  # Задание имени для файла, чтобы Telegram корректно обрабатывал

        bot.send_photo(message.chat.id, buf)
    except Exception as e:
        bot.send_message(message.chat.id, f'Произошла ошибка: {str(e)}. Проверьте правильность синтаксиса файла спектра.')


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
     /menu - маркап меню
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
     Кнопки снова работают!.\n
     Остальное на GitHub - https://GitHub.com/Nam4ik/SkPhys/
    ''')

@bot.message_handler(commands=['credits'])
def credits(message):
    bot.send_message(message.chat.id, "Создано командой Arcane Dev team и EvolveAI, @ArcaneDevStudio , @Evolve_AI. Для детей из Skchallenge. Контакт - @Nam4iks")

def AILOGIC(message, chat):
    bot.send_message(message.chat.id, "Введите промт")
    bot.register_next_step_handler(message, chat, AI)
def AI(message, chat):
    AI = 'GPT4o'
    
#    bot.send_message("ИИ Скоро ответит...")
    promt = message.text
    request_json = {
        "message": promt, 
        "api_key": CHAD_API_KEY
    }  
    bot.send_message(chat.id, "Введите промт") 
    answer = requests.post(url='https://ask.chadgpt.ru/api/public/gpt-4o-mini', answer=request_json)
    bot.send_message(f'{AI} ответил: {answer}')
    if "/AILogs" in message.text:
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


def rate_step(message):
    bot.send_message(message.chat.id, 'Введите вашу оценку. От 1 до 10')
    bot.register_next_step_handler(message, process_rating)

def process_rating(message):
    try:
        rate = int(message.text)
        if rate < 1 or rate > 10:
            bot.send_message(message.chat.id, "Ошибка! Оценка должна быть от 1 до 10.")
            return

        # Сохранение оценки
        with open('rates.json', 'r') as f:
            allrates = json.load(f)

        allrates.append(rate)
        with open('rates.json', 'w') as f:
            json.dump(allrates, f)

        bot.send_message(message.chat.id, 'Спасибо за оценку!')
    except ValueError:
        bot.send_message(message.chat.id, 'Ошибка! Пожалуйста, введите числовую оценку.')

def generate_plot(x_expr, y_expr):
    try:
        x = sp.symbols('x')
        y_expr = y_expr.replace('y', 'x')
        x_expr = sp.sympify(x_expr)
        y_expr = sp.sympify(y_expr)
        
        f_y = sp.lambdify(x, y_expr, "numpy")
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f_y(x_vals)

        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label=f'{y_expr} vs {x_expr}')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(f'График функции: {y_expr} vs {x_expr}')
        plt.grid(True)
        plt.legend()

        image_stream = io.BytesIO()
        plt.savefig(image_stream, format='png')
        image_stream.seek(0)
        plt.close()

        return image_stream
    except Exception as e:
        return str(e)

@bot.message_handler(commands=['plot'])
def handle_plot(message):
    # Извлекаем математическое выражение после команды
    math_expression = message.text[len('/plot '):].strip() 
    if not math_expression:
        bot.reply_to(message, "Пожалуйста, предоставьте математическое выражение.")
        return
    
    try:
        # Разделяем выражение на x и y
        math_expressions = math_expression.split(',')
        if len(math_expressions) == 2:
            x_expr = math_expressions[0].strip()
            y_expr = math_expressions[1].strip()
            
            plot_image = generate_plot(x_expr, y_expr)
            if isinstance(plot_image, str):
                bot.reply_to(message, f"Ошибка: {plot_image}")
            else:
                bot.send_photo(message.chat.id, plot_image)
        else:
            bot.reply_to(message, "Необходимо предоставить оба выражения, разделенные запятой.")
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")



@bot.message_handler(lambda message: message.text == 'График')
def process_plot(message):
    bot.send_message(message.chat.id, "Введите выражение для построения графика")
    math_expression = message.text
    if not math_expression:
        bot.reply_to(message, "Please provide a mathematical expression.")
        return
    try:
        math_expressions = math_expression.split(',')
        if len(math_expressions) == 2:
            x_expr = math_expressions[0].strip()
            y_expr = math_expressions[1].strip()
            
            plot_image = generate_plot(x_expr, y_expr)
            if isinstance(plot_image, str):
                bot.reply_to(message, f"Error: {plot_image}")
            else:
                bot.send_photo(message.chat.id, plot_image)
        else:
            bot.reply_to(message, "You need to provide both expressions separated by a comma.")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")


def last_rates(message, allrates, chat):
    int_values = [item for item in allrates if isinstance(item, int)]
    str_values = [item for item in allrates if isinstance(item, str)]
    irate = str_values[-5:]
    irateint = int_values[-5:]
    bot.send_message(chat.id, f'''
    Последние несколько отзывов. Текстовые: {irate}
    Числовой рейтинг: {irateint}''')

@bot.message_handler(commands=['rating'])
def callrating(message, chat):
    last_rates(message, chat)

@bot.message_handler(commands=['rate'])
def callratings(message):
    rate_step(message, message.chat)

@bot.message_handler(commands=['settings'])
def settings(message):
    pass

@bot.message_handler(commands=['AI'])
def callAI(message, chat):
    AILOGIC(message, chat)

@bot.message_handler(commands=['Rwave'])
def revW(message):
    bot.send_message(message.chat.id, 'Укажите значение для расчета обратной волны:')
    bot.register_next_step_handler(message, WaveRev())

#def process_reverse_wave_value(message):
#    try:
#        value = float(message.text)
#         Логика расчета здесь
#    except ValueError:
#        bot.send_message(message.chat.id, 'Ошибка! Убедитесь, что введено корректное значение.')

@bot.message_handler(commands=['Rflaser'])
def CallFlRev(message):
 pass 
#    fluenseRev(message, message.chat.id)

@bot.message_handler(commands=['wave'])
def CallWave(message):
    waveD(message, message.chat.id)

@bot.message_handler(commands=['flaser'])
def callFlaser(message):
    Flaser_script(message)

@bot.message_handler(commands=['CheightR'])
def callCheightr(message):
    CheightR(message, message.chat.id)

@bot.message_handler(commands=['Cheight help'])
def helpCheight(message):
    CheightR(message, message.chat.id)
                                                                                                                                                                                                 
   # Энергоэффективность топлива (константы)              
@bot.message_handler(commands=['Cheight'])
def callCheight(message, chat):
    Cheight(message, chat)

@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(func, fcredit, btn0, btn1, btn2)
    bot.send_message(message.chat.id, 'Меню открыто, проверьте клавиатуру.', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Функции')
def funckey(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(btn4, btn5, btn6, btn7, btn8, btnn, exit, fuelv)
    bot.send_message(message.chat.id, "Функции на вашей клавиатуре. Нажмите назад чтобы перейти в основное меню", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Назад")
def exitb(message): 
    bot.send_message(message.chat.id, "Основное меню")
    menu(message)

@bot.message_handler(func=lambda message: message.text == "ИИ")
def handle_ai(message, chat):
    AILOGIC(message, chat)

@bot.message_handler(func=lambda message: message.text == "О создателях")
def handle_credits(message):
    credits(message)

@bot.message_handler(func=lambda message: message.text == "Оценки")
def handle_rating(message):
    callrating(message, message.chat.id)

@bot.message_handler(func=lambda message: message.text == "Длина волны в частоту")
def handle_wavelength_to_frequency(message):
    Wave_bot(message)

@bot.message_handler(func=lambda message: message.text == "Помощь")
def help2(message):
    help(message)

@bot.message_handler(func=lambda message: message.text == "Флюенс лазерной системы")
def Flasercall(message):
    Flaser_script(message)
def rate_step(message):
    bot.send_message(message.chat.id, 'Введите вашу оценку. От 1 до 10')
    bot.register_next_step_handler(message, process_rating)

def process_rating(message):
    try:
        rate = int(message.text)
        if rate < 1 or rate > 10:
            bot.send_message(message.chat.id, "Ошибка! Оценка должна быть от 1 до 10.")
            return

        # Сохранение оценки
        with open('rates.json', 'r') as f:
            allrates = json.load(f)
    except FileNotFoundError:
        allrates = []
#Flaser_script(message)

@bot.message_handler(commands=['AI'])
def ai(message):
    AI(message)

@bot.message_handler(func=lambda message: message.text == "Колебательный контур")
def circ(message):
    circuitq(message)

@bot.message_handler(func=lambda message: message.text == "Виды отопления и их цена")
def call_heating_cost(message):
    your_sqare(message)
bot.polling(none_stop=True)
