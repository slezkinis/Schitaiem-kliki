import os
import requests
import argparse

import urllib.parse
from dotenv import load_dotenv


def shorten_link(bitlink_token, long_url):
    api_bitlink_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    payload = {
        'long_url': long_url
    }
    headers = {
        'Authorization': f'Bearer {bitlink_token}'
    }
    response = requests.post(api_bitlink_url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(bitlink_token, short_url):
    url_parts = urllib.parse.urlparse(short_url)
    bitlink_url = f'{url_parts.netloc}{url_parts.path}'
    headers = {
        'Authorization': f'Bearer {bitlink_token}'
    }
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_url}/clicks/summary',
        headers=headers
    )
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(user_url, bitlink_token):
    url_parts = urllib.parse.urlparse(user_url)
    bitlink_url = f'{url_parts.netloc}{url_parts.path}'
    headers = {
        'Authorization': f'Bearer {bitlink_token}'
    }
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_url}',
        headers=headers
    )
    return response.ok


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Программа конвертирует ссылки'
    )
    parser.add_argument('link', help='Ваша фамилия')
    args = parser.parse_args()
    bitlink_token = os.environ['BITLINK_TOKEN']
    user_input = args.link
    try:
        if is_bitlink(user_input, bitlink_token):
            print(f'Число кликов: {count_clicks(bitlink_token, user_input)}')
        else:
            print(f'Битлинк: {shorten_link(bitlink_token, user_input)}')
    except requests.exceptions.HTTPError:
        print('Cсылка некорректна')
