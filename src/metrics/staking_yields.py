import requests

def get_staking_yields():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": False
    }
    response = requests.get(url, params=params)
    data = response.json()

    staking_yields = {}
    for coin in data:
        if 'staking_yield' in coin:
            staking_yields[coin['id']] = {
                'name': coin['name'],
                'staking_yield': coin['staking_yield']
            }
    
    return staking_yields