def get_spot_prices():
    import requests

    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,solana,cardano",
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    data = response.json()

    prices = {
        "bitcoin": data['bitcoin']['usd'],
        "ethereum": data['ethereum']['usd'],
        "solana": data['solana']['usd'],
        "cardano": data['cardano']['usd']
    }
    return prices

def display_spot_prices(prices):
    for crypto, price in prices.items():
        print(f"{crypto.capitalize()}: ${price:,.2f}")