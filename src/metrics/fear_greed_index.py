import requests

def get_fear_greed_index():
    url = "https://api.alternative.me/fng/"
    response = requests.get(url)
    data = response.json()
    if 'data' in data and len(data['data']) > 0:
        fear_greed_index = data['data'][0]['value']
        sentiment = data['data'][0]['sentiment']
        return fear_greed_index, sentiment
    else:
        raise Exception("Error retrieving Fear and Greed Index data")