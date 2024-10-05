import requests
from config import settings


def send_telegram_message(tg_chat_id, message):
    params = {
        'chat_id': tg_chat_id,
        'text': message,
    }
    requests.get(f'{settings.TELEGRAM_URL}/bot{settings.TELEGRAM_TOKEN}/sendMessage', params=params).json()
