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
