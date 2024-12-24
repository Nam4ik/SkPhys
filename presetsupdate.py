import json
import requests
import time

# Функция для загрузки цен
def load_prices():
    url = 'https://prices.openfoodfacts.org/api/schema?format=json&lang=ru'
    
    # Выполняем GET-запрос
    response = requests.get(url)
    
    # Проверяем, успешен ли запрос
    if response.status_code == 200:
        # Получаем JSON-данные из ответа
        data = response.json()
        
        # Сохраняем данные в файл
        with open("valuepresets.json", "w", encoding='utf-8') as valuesw:
            json.dump(data, valuesw, ensure_ascii=False, indent=4)
        print("Данные успешно загружены и сохранены в valuepresets.json")
    else:
        print(f"Ошибка при загрузке данных: {response.status_code}")

