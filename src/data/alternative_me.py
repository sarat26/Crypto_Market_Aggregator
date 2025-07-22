import requests

def get_fear_and_greed_index():
    url = "https://api.alternative.me/fng/"
    response = requests.get(url)
    data = response.json()
    if 'data' in data and len(data['data']) > 0:
        index_value = data['data'][0]['value']
        index_label = data['data'][0]['label']
        return index_value, index_label
    else:
        return None, None