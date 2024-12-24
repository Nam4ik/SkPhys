import pytest
from unittest.mock import Mock, patch
import numpy as np
import json
import io
from TeleBot import (
    power_to_fluence,
    get_exchange_rates,
    choosing_a_heating_source,
    Wave_script
)

# Фикстуры для моков
@pytest.fixture
def mock_bot():
    return Mock()

@pytest.fixture
def mock_message():
    message = Mock()
    message.chat.id = 123
    message.text = "Test message"
    return message

# Тесты физических расчетов
def test_power_to_fluence():
    power = 100  # Вт
    area = 2    # см²
    time = 5    # сек
    expected = 10  # Дж/см²
    result = power_to_fluence(power, area, time)
    assert result == expected

# Тест волновых расчетов
@patch('SkPhys.Expiremental.TeleBot.bot')
def test_wave_script(mock_bot, mock_message):
    mock_message.text = "500e-9"  # 500 нм
    Wave_script(mock_message)
    expected_freq = 6e14  # Гц
    mock_bot.send_message.assert_called_with(
        mock_message.chat.id,
        f'Частота волны равна {round(expected_freq, 1)} Гц или {round(expected_freq/1e6, 1)} Мгц'
    )

# Тест курсов валют
@patch('requests.get')
def test_get_exchange_rates(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        'rates': {
            'USD': 0.011,
            'EUR': 0.010
        }
    }
    mock_get.return_value = mock_response
    
    usd_rate, eur_rate = get_exchange_rates()
    assert usd_rate == 0.011
    assert eur_rate == 0.010

# Тест расчета отопления
def test_choosing_a_heating_source():
    your_squares = 100
    result = choosing_a_heating_source(your_squares)
    assert len(result) == 3
    assert all(isinstance(x, (int, float)) for x in result)

# Тест обработки спектра
def test_spectrum_processing():
    # Создаем тестовые данные
    x = np.linspace(0, 10, 100)
    y = np.sin(x) + 1
    test_data = np.column_stack((x, y))
    
    # Сохраняем во временный файл
    np.savetxt('test_spectrum.txt', test_data)
    
    # Проверяем загрузку и обработку
    data = np.loadtxt('test_spectrum.txt')
    assert data.shape == (100, 2)
    assert np.allclose(data[:, 0], x)
    assert np.allclose(data[:, 1], y)

# Тест сохранения оценок
def test_rating_system():
    test_rates = [5, 7, 8, 9, 10]
    with open('test_rates.json', 'w') as f:
        json.dump(test_rates, f)
        
    with open('test_rates.json', 'r') as f:
        loaded_rates = json.load(f)
    
    assert loaded_rates == test_rates
    assert min(loaded_rates) >= 1
    assert max(loaded_rates) <= 10

if __name__ == '__main__':
    pytest.main(['-v'])
