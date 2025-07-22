import requests

def get_spot_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,solana,cardano",
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return {
        "bitcoin": data['bitcoin']['usd'],
        "ethereum": data['ethereum']['usd'],
        "solana": data['solana']['usd'],
        "cardano": data['cardano']['usd']
    }

def get_market_data():
    spot_prices = get_spot_prices()
    # Additional metrics can be retrieved and calculated here
    return spot_prices