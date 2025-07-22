import requests

def get_borrow_lend_rates():
    # Example API endpoints for borrow and lend rates
    borrow_url = "https://api.example.com/borrow_rates"
    lend_url = "https://api.example.com/lend_rates"
    
    # Fetch borrow rates
    borrow_response = requests.get(borrow_url)
    borrow_data = borrow_response.json()
    
    # Fetch lend rates
    lend_response = requests.get(lend_url)
    lend_data = lend_response.json()
    
    # Extract relevant data
    borrow_rates = {item['currency']: item['rate'] for item in borrow_data['rates']}
    lend_rates = {item['currency']: item['rate'] for item in lend_data['rates']}
    
    return borrow_rates, lend_rates

def calculate_average_rates(borrow_rates, lend_rates):
    average_rates = {}
    for currency in borrow_rates.keys():
        average_rates[currency] = {
            'borrow_rate': borrow_rates[currency],
            'lend_rate': lend_rates.get(currency, None)
        }
    return average_rates