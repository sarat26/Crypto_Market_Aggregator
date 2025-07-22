def calculate_delta_skew(options_data):
    """
    Calculate the 25-delta skew for options based on the provided options data.
    
    Parameters:
    options_data (list): A list of dictionaries containing options data with 'strike_price', 'bid', and 'ask' keys.

    Returns:
    float: The calculated 25-delta skew. 
    """
    # Filter for out-of-the-money puts and calls
    puts = [option for option in options_data if option['bid'] < option['ask']]
    calls = [option for option in options_data if option['bid'] > option['ask']]

    # Calculate the implied volatility for puts and calls
    put_iv = sum(option['bid'] for option in puts) / len(puts) if puts else 0
    call_iv = sum(option['ask'] for option in calls) / len(calls) if calls else 0

    # Calculate the 25-delta skew
    delta_skew = (put_iv - call_iv) / (put_iv + call_iv) * 100 if (put_iv + call_iv) != 0 else 0

    return delta_skew

def get_options_data(api_response):
    """
    Extract options data from the API response.

    Parameters:
    api_response (dict): The response from the options data API.

    Returns:
    list: A list of dictionaries containing relevant options data.
    """
    options_data = []
    for option in api_response['options']:
        options_data.append({
            'strike_price': option['strike'],
            'bid': option['bid'],
            'ask': option['ask']
        })
    return options_data

def fetch_delta_skew(api_url):
    """
    Fetch options data from the specified API URL and calculate the delta skew.

    Parameters:
    api_url (str): The URL of the API to fetch options data from.

    Returns:
    float: The calculated delta skew.
    """
    response = requests.get(api_url)
    if response.status_code == 200:
        options_data = get_options_data(response.json())
        return calculate_delta_skew(options_data)
    else:
        raise Exception("Failed to fetch data from API")