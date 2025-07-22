import requests

def get_perpetual_funding_rates():
    url = "https://www.deribit.com/api/v2/public/get_funding_rate"
    response = requests.get(url)
    data = response.json()
    funding_rates = data['result']
    return funding_rates

def get_open_interest():
    url = "https://www.deribit.com/api/v2/public/get_open_interest"
    response = requests.get(url)
    data = response.json()
    open_interest = data['result']
    return open_interest

def get_derivatives_metrics():
    funding_rates = get_perpetual_funding_rates()
    open_interest = get_open_interest()
    return {
        "funding_rates": funding_rates,
        "open_interest": open_interest
    }