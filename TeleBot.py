

import telebot
from telebot import types
import numpy as np
from scipy.signal import find_peaks
import math
import requests
import os
import json
import matplotlib.pyplot as plt
import io
import api

flags = ['/rev', '/exc']
bot = telebot.TeleBot(api.API_TOKEN)
Langs = ['Ru', 'En']
Lang = "Ru"
Outputs = ['.txt', 'message']
Output = ['.txt']
Credits = "Bot created by Arcane Dev team and EvolveAI"
lightspeed = 300000000
lightspedt = 299792458
CHAD_API_KEY = api.CHAD_API_KEY
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
exit = types.KeyboardButton('Назад')
func = types.KeyboardButton('Функции')
fcredit = types.KeyboardButton('О создателях')
reply = types.KeyboardButton('Связаться с нами')
btn = types.KeyboardButton('Настройки')
btn0 = types.KeyboardButton('ИИ')
btn1 = types.KeyboardButton('Помощь')
btn2 = types.KeyboardButton('Оценки')
btn3 = types.KeyboardButton('Посмотреть оценки')
btn4 = types.KeyboardButton('Флюенс лазерной системы')
btn5 = types.KeyboardButton('Мощность лазерной системы')
btn6 = types.KeyboardButton('Пик и его ширина в полувысоте')
btn7 = types.KeyboardButton('Частота излучения в длину волны')
btn8 = types.KeyboardButton('Длина волны в частоту')
btnn = types.KeyboardButton('Колебательный контур')

@bot.message_handler(commands=['start'])
def welcome(message):
    markup.add(btn, btn1, btn2, btn3)
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

def Flaser_script(message, chat):
    bot.send_message(chat.id ,"Укажите значение мощности лазерной системы в Wt (int)")
    args = message.text.split()

    try:
        power = float(args)
        bot.send_message(message.chat.id, 'Напишите площадь (см²)')
        bot.register_next_step_handler(message, process_area, power)
    except ValueError:
        bot.reply_to(message, 'Ошибка! Убедитесь, что мощность указана правильно.')

def process_area(message, power):
    try:
        area = float(message.text)
        bot.send_message(message.chat.id, 'Теперь отправьте время (секунды)!')
        bot.register_next_step_handler(message, process_time, power, area)
    except ValueError:
        bot.send_message(message.chat.id, 'Ошибка! Пожалуйста, введите площадь в числовом формате.')

def process_time(message, power, area):
    try:
        time = float(message.text)
        fluence = power_to_fluence(power, area, time)
        bot.reply_to(message, f'Флюенс: {fluence:.2f} Дж/см²')
    except ValueError:
        bot.send_message(message.chat.id, 'Ошибка! Пожалуйста, введите время в числовом формате.')

# Удаляем ненужные raise и обрабатываем исключения
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

def Cheight(message, chat):
    with open("specrum.txt", "r") as spectr:
        spectr.read
        if spectr.read==True:
            bot.send_message(chat.id ,"Файл загружен")
    try:
        data = np.loadtxt(spectr)
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
        bot.send_message(message.chat.id, 'Произошла ошибка при обработке файла спектра. Проверьте правильность синтаксиса на https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html')

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

def AI(message, chat):
    AI = 'GPT4o'
    request_json = {
        "message": "Как думаешь, сколько будет 2+9?",
        "api_key": CHAD_API_KEY
    }
    bot.send_message(chat.id, "Введите промт")
    promt = message.text 
    global answer
    requests.post(url='https://ask.chadgpt.ru/api/public/gpt-4o-mini', answer=request_json)
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

@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(func, fcredit, btn0, btn1, btn2)
    bot.send_message(message.chat.id, 'Меню открыто, проверьте клавиатуру.', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Функции')
def funckey(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(btn4, btn5, btn6, btn7, btn8, btnn, exit)
    bot.send_message(message.chat.id, "Функции на вашей клавиатуре. Нажмите назад чтобы перейти в основное меню", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Назад")
def exitb(message): 
    bot.send_message(message.chat.id, "Основное меню")
    menu(message)

@bot.message_handler(func=lambda message: message.text == "ИИ")
def handle_ai(message):
    AI(message)

@bot.message_handler(func=lambda message: message.text == "О создателях")
def handle_credits(message):
    credits(message)

@bot.message_handler(func=lambda message: message.text == "Оценки")
def handle_rating(message):
    callrating(message)

@bot.message_handler(func=lambda message: message.text == "Длина волны в частоту")
def handle_wavelength_to_frequency(message):
    Wave_script(message)
@bot.message_handler(func=lambda message: message.text == "Помощь")
def help2(message):
    help(message)
@bot.message_handler(func=lambda message: message.text == "Пик и его ширина в полувысоте")
def cheightcall(message, file_path):
  Cheight(message, file_path)
bot.polling()
