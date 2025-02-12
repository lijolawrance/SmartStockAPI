from sqlalchemy.orm import Session
from app.models import Stock


def insert_stock(db: Session, stock_data: dict):
    """Always insert a new stock record without updating"""
    try:
        print(
            f"🆕 Inserting new stock record for {stock_data['symbol']} at {stock_data['timestamp']}"
        )
        stock = Stock(
            **stock_data
        )  # No need to set `id`, PostgreSQL will auto-generate it
        db.add(stock)
        db.commit()
        db.refresh(stock)  # Get the latest committed data
        return stock
    finally:
        db.close()  # ✅ Ensure the session is always closed


def get_latest_stock(db: Session, symbol: str):
    """Fetch the most recent stock record based on timestamp"""
    try:
        return (
            db.query(Stock)
            .filter(Stock.symbol == symbol)
            .order_by(Stock.timestamp.desc())  # Sort by latest timestamp
            .first()
        )
    finally:
        db.close()  # ✅ Always close the session after querying


def get_stock_history(db: Session, symbol: str, limit: int = 10):
    """Fetch the historical stock data for a given symbol"""
    try:
        return (
            db.query(Stock)
            .filter(Stock.symbol == symbol)
            .order_by(Stock.timestamp.desc())  # Latest first
            .limit(limit)  # Optional limit for performance
            .all()
        )
    finally:
        db.close()  # ✅ Always close the session
