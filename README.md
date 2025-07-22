# Crypto Market Data Aggregator

This project is a comprehensive cryptocurrency market data aggregator that retrieves public market data from various APIs, including CoinGecko, CoinGlass, Binance, Deribit, and Alternative.me. The focus is on gathering key metrics such as spot prices, realized volatility, funding rates, futures basis, open interest, delta skew, borrow/lend rates, staking yields, and the fear and greed index. The aggregated data is then formatted into a PDF report for weekly updates to institutional clients.

## Project Structure

```
crypto-market-aggregator
├── src
│   ├── __init__.py
│   ├── main.py                # Entry point for the application
│   ├── data                   # Module for data retrieval from APIs
│   │   ├── __init__.py
│   │   ├── coingecko.py       # Functions for CoinGecko API
│   │   ├── coinglass.py       # Functions for CoinGlass API
│   │   ├── binance.py         # Functions for Binance API
│   │   ├── deribit.py         # Functions for Deribit API
│   │   ├── alternative_me.py   # Functions for Alternative.me API
│   ├── metrics                # Module for calculating various metrics
│   │   ├── __init__.py
│   │   ├── spot_prices.py      # Spot prices calculations
│   │   ├── realized_volatility.py # Realized volatility calculations
│   │   ├── funding_rates.py    # Funding rates calculations
│   │   ├── futures_basis.py    # Futures basis calculations
│   │   ├── open_interest.py     # Open interest calculations
│   │   ├── delta_skew.py       # Delta skew calculations
│   │   ├── borrow_lend_rates.py # Borrow and lend rates calculations
│   │   ├── staking_yields.py    # Staking yields calculations
│   │   └── fear_greed_index.py  # Fear and Greed Index retrieval
│   ├── report                 # Module for report generation
│   │   ├── __init__.py
│   │   └── pdf_generator.py     # PDF report generation functions
│   └── utils                  # Utility functions
│       ├── __init__.py
│       └── helpers.py          # Helper functions for data processing
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd crypto-market-aggregator
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Metrics Tracked

- **Spot Prices**: Current market prices for various cryptocurrencies.
- **Realized Volatility**: Measures the volatility of selected cryptocurrencies over 7-day and 30-day periods.
- **Funding Rates**: Rates that determine the cost of holding a position in perpetual contracts.
- **Futures Basis**: The difference between the spot price and the futures price of a cryptocurrency.
- **Open Interest**: Total number of outstanding derivative contracts.
- **Delta Skew**: A measure of the difference in implied volatility between out-of-the-money puts and calls.
- **Borrow/Lend Rates**: Rates for borrowing and lending cryptocurrencies.
- **Staking Yields**: Returns from staking various cryptocurrencies.
- **Fear and Greed Index**: A sentiment analysis index that gauges market emotions.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.