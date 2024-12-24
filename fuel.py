import pandas as pd
import telebot 
import io
import api 
bot = telebot.TeleBot(api.API_TOKEN)
def fuel(message):
  data = {
'Вид толпива': ['Газ (1M^3)', 'Дрова (Кг)', 'Газ в баллонах (Л)'], 
'Энергоэффективность (кВт/Час)': [10.62, 4.66, 7.33]
}

  row_labels = [1, 2, 3]
  df = pd.DataFrame(data=data, index=row_labels)
  print(df)
  df.to_csv('data_tabel.csv', index=False, encoding='utf-8')
  buf = io.BytesIO(df, "png")
  bot.send_image(message.chat.id, buf)