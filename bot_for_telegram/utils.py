import json
import numpy as np
import requests
from config import keys, APIKEY

class ConvertionExeption(Exception):
    pass

class CriptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionExeption(f"Невозможно перевести одинаковые вылюты {base}.")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f"Не удалось обработать валюту {quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f"Не удалось обработать валюту {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f"Не удалось обработать количество {amount}")

        r = requests.get((f'https://currate.ru/api/?get=rates&pairs={quote_ticker}{base_ticker}&key={APIKEY}'))
        text = json.loads(r.content)['data'][f'{keys[quote]}{keys[base]}']    #перевод json-a на Python. Квадратные скобки - ?
        result = np.round(float(text) * float(amount), 2)

        return result
