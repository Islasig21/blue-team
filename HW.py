'''import os 
from coinmarketcapapi import CoinMarketCapAPI
apikey = "Your Api Key"
cmc = CoinMarketCapAPI(apikey)
info = cmc.cryptocurrency_info(symbol="SOL")
print(info.data.get("SOL,{}"))


quotes = cmc.cryptocurrency_quotes_latest(symbol="SOL", convert = "USD")
solana_data = quotes.data["SOL"]["quote"]["USD"]
print(solana_data)

'''
'''
import os
import requests

class SolanaCMCRequests:
    BASE_URL = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"

    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("CMC_KEY")
        if not self.api_key:
            raise ValueError("API key is required")
        self.session = requests.Session()
        self.session.headers.update({
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": self.api_key,
        })

    def get_quote(self, symbol="SOL", convert="USD"):
        params = {"symbol": symbol, "convert": convert}
        resp = self.session.get(self.BASE_URL, params=params)
        resp.raise_for_status()
        data = resp.json()
        return data["data"][symbol]["quote"][convert]   # هنا التصحيح

# مثال:
if __name__ == "__main__":
    sol = SolanaCMCRequests(api_key="YOUR_API_KEY")
    print(sol.get_quote())
'''
'''hw'''

import requests

class CoinMarketCapSolana:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

    def get_solana_data(self):
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.api_key,
        }
        parameters = {
            'symbol': 'SOL',
            'convert': 'USD'
        }
        try:
            response = requests.get(self.base_url, headers=headers, params=parameters)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def export_solana_data(self, data, filename="solana_data.txt"):
        if data:
            with open(filename, 'w') as f:
                f.write(str(data))
            print(f"Data exported to {filename}")
        else:
            print("No data to export.")


