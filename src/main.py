import requests
from datetime import datetime
from data.coingecko import get_spot_prices
from data.coinglass import get_funding_rates, get_open_interest
from data.binance import get_futures_basis, get_delta_skew
from data.deribit import get_perpetual_funding_rates
from data.alternative_me import get_fear_and_greed_index
from metrics.spot_prices import calculate_spot_prices
from metrics.realized_volatility import calculate_realized_volatility
from metrics.funding_rates import calculate_funding_rates
from metrics.futures_basis import calculate_futures_basis
from metrics.open_interest import calculate_open_interest
from metrics.delta_skew import calculate_delta_skew
from metrics.borrow_lend_rates import calculate_borrow_lend_rates
from metrics.staking_yields import calculate_staking_yields
from metrics.fear_greed_index import calculate_fear_greed_index
from report.pdf_generator import generate_pdf_report

def get_spot_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,solana,cardano",
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["bitcoin"]["usd"], data["ethereum"]["usd"], data["solana"]["usd"], data["cardano"]["usd"]

def main():
    date = datetime.now().strftime("%B %d, %Y")
    print(f"Crypto Market Data Aggregator -- {date}\n")

    # Retrieve data from APIs
    btc_price, eth_price, sol_price, ada_price = get_spot_prices()
    funding_rates = get_funding_rates()
    open_interest = get_open_interest()
    futures_basis = get_futures_basis()
    delta_skew = get_delta_skew()
    perpetual_funding_rates = get_perpetual_funding_rates()
    fear_and_greed_index = get_fear_and_greed_index()

    # Calculate metrics
    spot_prices = calculate_spot_prices(btc_price, eth_price, sol_price, ada_price)
    realized_volatility = calculate_realized_volatility()
    funding_rates_metrics = calculate_funding_rates(funding_rates)
    futures_basis_metrics = calculate_futures_basis(futures_basis)
    open_interest_metrics = calculate_open_interest(open_interest)
    delta_skew_metrics = calculate_delta_skew(delta_skew)
    borrow_lend_rates_metrics = calculate_borrow_lend_rates()
    staking_yields_metrics = calculate_staking_yields()
    fear_greed_index_metrics = calculate_fear_greed_index(fear_and_greed_index)

    # Generate PDF report
    generate_pdf_report(spot_prices, realized_volatility, funding_rates_metrics, 
                         futures_basis_metrics, open_interest_metrics, 
                         delta_skew_metrics, borrow_lend_rates_metrics, 
                         staking_yields_metrics, fear_greed_index_metrics)

if __name__ == "__main__":
    main()

