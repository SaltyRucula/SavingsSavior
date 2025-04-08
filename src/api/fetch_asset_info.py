import httpx
import dotenv
import os

dotenv.load_dotenv()
api_key = os.getenv("API_KEY")


def fetch_asset_info(symbol: str):
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}"
    response = httpx.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Error:", response.status_code)
