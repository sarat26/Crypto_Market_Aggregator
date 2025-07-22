import requests

def get_funding_rates():
    url = "https://api.coinglass.com/api/pro/v1/funding_rate"
    headers = {
        "accept": "application/json",
        "X-API-KEY": "your_api_key_here"  # Replace with your actual API key
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

def get_open_interest():
    url = "https://api.coinglass.com/api/pro/v1/open_interest"
    headers = {
        "accept": "application/json",
        "X-API-KEY": "your_api_key_here"  # Replace with your actual API key
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data