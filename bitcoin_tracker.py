import requests
import numpy as np
import matplotlib.pyplot as plt
from termcolor import colored
from pycoingecko import CoinGeckoAPI
from datetime import datetime, timedelta

def get_crypto_price(crypto_id, currency, days=365):
    try:
        cg = CoinGeckoAPI()
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        # Convert dates to timestamps
        start_timestamp = int(start_date.timestamp())
        end_timestamp = int(end_date.timestamp())

        data = cg.get_coin_market_chart_range_by_id(
            id=crypto_id, vs_currency=currency, from_timestamp=start_timestamp, to_timestamp=end_timestamp, days=days
        )

        if "prices" in data and isinstance(data["prices"], list):
            price_data = {}
            for entry in data["prices"]:
                date = entry[0] / 1000
                price = entry[1]
                price_data[date] = price
            return price_data
        else:
            raise KeyError("Invalid response format")
    except requests.RequestException as e:
        print(colored(f"Error: Failed to retrieve crypto price data - {e}", 'red'))
        return None
    except KeyError as e:
        print(colored(f"Error: Invalid response - {e}", 'red'))
        return None

def plot_crypto_price(crypto_data, currency, crypto_id):
    if crypto_data is not None:
        dates = sorted(list(crypto_data.keys()))
        prices = [crypto_data[date] for date in dates]

        if len(prices) >= 30:
            # Calculate 30-day moving average
            moving_average = np.convolve(prices, np.ones(30)/30, mode='valid')
            start_idx = 29  # Index to start plotting moving average

            plt.figure(figsize=(12, 6))
            plt.plot(dates[start_idx:], moving_average, label=f'{currency} 30-day MA', color='blue')
        else:
            start_idx = 0

        plt.plot(dates, prices, label=f'{currency} Price', color='orange', linewidth=2)
        plt.title(colored(f"{crypto_id.upper()} Price vs. {currency.upper()} with 30-day Moving Average", 'blue'))
        plt.xlabel("Date")
        plt.ylabel(f"Price ({currency.upper()})")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()
    else:
       print(colored("Error: Failed to retrieve crypto price data.", 'red'))

def main():
    # Customize the cryptocurrency and currency here
    crypto_id = 'bitcoin'  # Keep it as 'bitcoin' to analyze Bitcoin
    currency = 'usd'       # Customize currency

    print(colored(f"Fetching {crypto_id.upper()} price data in {currency.upper()}...", 'cyan'))
    crypto_price_data = get_crypto_price(crypto_id, currency)
    if crypto_price_data is not None:
        plot_crypto_price(crypto_price_data, currency, crypto_id)
    else:
        print(colored("Error: Failed to retrieve crypto price data.", 'red'))

if __name__ == "__main__":
    main()

