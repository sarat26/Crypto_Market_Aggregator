def get_open_interest(symbol):
    url = f"https://api.example.com/open_interest/{symbol}"  # Replace with actual API endpoint
    response = requests.get(url)
    data = response.json()
    return data['open_interest']

def calculate_open_interest(contracts):
    total_open_interest = sum(contract['open_interest'] for contract in contracts)
    return total_open_interest

def get_all_open_interest(symbols):
    open_interest_data = {}
    for symbol in symbols:
        open_interest = get_open_interest(symbol)
        open_interest_data[symbol] = open_interest
    return open_interest_data