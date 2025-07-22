def format_currency(value):
    return f"${value:,.2f}"

def format_percentage(value):
    return f"{value:.2f}%"

def current_timestamp():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validate_response(response):
    if response.status_code != 200:
        raise ValueError(f"Error fetching data: {response.status_code} - {response.text}")

def extract_data(data, keys):
    return {key: data.get(key) for key in keys}