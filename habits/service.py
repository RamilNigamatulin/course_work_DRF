import requests
from config import settings


def send_telegram_message(chat_id, text):
    params = {
        'chat_id': chat_id,
        'text': text,
    }
    response = requests.get(f'{settings.TELEGRAM_URL}/bot{settings.TELEGRAM_TOKEN}/sendMessage', params=params)
    if response.status_code == 200:
        print("Сообщение успешно отправлено!")
    else:
        print(f"Ошибка при отправке сообщения: {response.status_code} - {response.text}")
