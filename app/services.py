import requests
import os
from dotenv import load_dotenv
import datetime

# Load environment variables
load_dotenv()

API_KEY = os.getenv("FMP_CLOUD_API_KEY")
API_URL = "https://financialmodelingprep.com/api/v3/quote"


def fetch_stock_price(symbol: str):
    """Fetch full stock data from FMP Cloud API"""
    if not API_KEY:
        print("❌ Error: FMP_CLOUD_API_KEY is missing in .env file")
        return None

    url = f"{API_URL}/{symbol}?apikey={API_KEY}"
    response = requests.get(url)

    print("🔍 API Response:", response.text)  # Debugging print

    if response.status_code != 200:
        return None  # Handle API errors

    data = response.json()

    if not data or not isinstance(data, list) or "symbol" not in data[0]:
        return None  # Handle missing data

    stock = data[0]

    # ✅ Convert timestamp correctly from milliseconds to seconds
    raw_timestamp = stock.get("timestamp")  # Comes in milliseconds
    if raw_timestamp:
        stock_timestamp = datetime.datetime.utcfromtimestamp(
            raw_timestamp
        )  # ✅ FIX: No need to divide by 1000
    else:
        stock_timestamp = datetime.datetime.utcnow()  # Use current timestamp if missing

    print(f"✅ Converted timestamp: {stock_timestamp}")  # Debugging print

    return {
        "symbol": stock.get("symbol"),
        "name": stock.get("name"),
        "price": stock.get("price"),
        "changes_percentage": stock.get("changesPercentage"),
        "change": stock.get("change"),
        "day_low": stock.get("dayLow"),
        "day_high": stock.get("dayHigh"),
        "year_high": stock.get("yearHigh"),
        "year_low": stock.get("yearLow"),
        "market_cap": stock.get("marketCap"),
        "price_avg_50": stock.get("priceAvg50"),
        "price_avg_200": stock.get("priceAvg200"),
        "exchange": stock.get("exchange"),
        "volume": stock.get("volume"),
        "avg_volume": stock.get("avgVolume"),
        "open_price": stock.get("open"),
        "previous_close": stock.get("previousClose"),
        "eps": stock.get("eps"),
        "pe": stock.get("pe"),
        "earnings_announcement": stock.get("earningsAnnouncement"),
        "shares_outstanding": stock.get("sharesOutstanding"),
        "timestamp": stock_timestamp,  # ✅ Now correctly converted
    }
