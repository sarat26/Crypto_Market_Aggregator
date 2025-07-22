def get_funding_rates():
    import requests

    # Example API endpoint for Deribit funding rates
    url = "https://www.deribit.com/api/v2/public/get_funding_rate"
    response = requests.get(url)
    data = response.json()

    funding_rates = {}
    if data['result']:
        for rate in data['result']:
            funding_rates[rate['instrument_name']] = rate['funding_8h']

    return funding_rates

def calculate_average_funding_rate(funding_rates):
    if not funding_rates:
        return 0
    return sum(funding_rates.values()) / len(funding_rates)