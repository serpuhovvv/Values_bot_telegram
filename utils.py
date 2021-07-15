import json
import requests
from config import keys


class ExchangeException(Exception):
    pass


class Exchange:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ExchangeException(f'Нельзя перевести одинаковые валюты {base}.')

        try:
            quote = keys[quote]
        except KeyError:
            raise ExchangeException(f'Не смог обработать валюту {quote}')

        try:
            base = keys[base]
        except KeyError:
            raise ExchangeException(f'Не смог обработать валюту {base}')

        try:
            amount = int(amount)
        except ValueError:
            raise ExchangeException(f'Не смог обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price/?fsum={keys[quote]}&tsyms={keys[base]})')
        total_base = json.loads(r.content)[keys[base]]
        text = f'Цена {amount}{quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

        return total_base
