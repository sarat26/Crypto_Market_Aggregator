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

def calculate_spot_prices(btc_price, eth_price, sol_price, ada_price):
    return {
        "BTC": btc_price,
        "ETH": eth_price,
        "SOL": sol_price,
        "ADA": ada_price
    }