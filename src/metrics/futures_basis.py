def calculate_futures_basis(futures_price, spot_price):
    return futures_price - spot_price

def get_futures_data(api_client):
    futures_data = api_client.get_futures_data()
    return futures_data

def calculate_three_month_futures_basis(api_client):
    futures_data = get_futures_data(api_client)
    spot_price = futures_data['spot_price']
    futures_price = futures_data['futures_price']
    
    basis = calculate_futures_basis(futures_price, spot_price)
    return basis