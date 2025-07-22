import requests

def get_futures_basis(symbol='BTCUSDT'):
    url = f'https://api.binance.com/api/v3/futures/data/basis'
    params = {
        'symbol': symbol,
        'limit': 1
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def get_delta_skew(symbol='BTCUSDT'):
    url = f'https://api.binance.com/api/v3/options/deltaSkew'
    params = {
        'symbol': symbol
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data