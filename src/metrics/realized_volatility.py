def calculate_realized_volatility(prices, window=7):
    if len(prices) < window:
        raise ValueError("Not enough data points to calculate realized volatility.")
    
    log_returns = [math.log(prices[i] / prices[i - 1]) for i in range(1, len(prices))]
    volatility = np.std(log_returns[-window:]) * np.sqrt(252)  # Annualized volatility
    return volatility

def get_7_day_realized_volatility(prices):
    return calculate_realized_volatility(prices, window=7)

def get_30_day_realized_volatility(prices):
    return calculate_realized_volatility(prices, window=30)