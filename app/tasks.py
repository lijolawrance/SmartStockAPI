from app.celery_worker import celery
from app.database import SessionLocal
from app.services import fetch_stock_price
from app.crud import insert_stock
import datetime


@celery.task
def update_stock_price(symbol: str):
    """Fetch and insert new stock price record (No Updates)."""
    db = SessionLocal()
    try:
        stock_data = fetch_stock_price(symbol)

        if stock_data:
            # ✅ Ensure timestamp is correctly converted to `datetime`
            if isinstance(stock_data["timestamp"], int):
                stock_data["timestamp"] = datetime.datetime.utcfromtimestamp(
                    stock_data["timestamp"]
                )

            insert_stock(db, stock_data)  # ✅ Only inserts, does not update
            return f"✅ Inserted new stock price record for {symbol}"
        else:
            return f"❌ Failed to fetch stock price for {symbol}"
    finally:
        db.close()  # ✅ Ensure Celery always releases the connection
