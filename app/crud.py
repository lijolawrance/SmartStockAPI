from sqlalchemy.orm import Session
from app.models import Stock

def get_stock(db: Session, symbol: str):
    """Retrieve stock data from the database"""
    return db.query(Stock).filter(Stock.symbol == symbol).first()

def add_stock(db: Session, stock_data: dict):
    """Insert or update full stock data in the database"""
    stock = get_stock(db, stock_data["symbol"])
    
    if stock:
        print(f"🔄 Updating stock: {stock_data['symbol']}")
        for key, value in stock_data.items():
            setattr(stock, key, value)
    else:
        print(f"🆕 Adding new stock: {stock_data['symbol']}")
        stock = Stock(**stock_data)
        db.add(stock)
    
    db.commit()
    db.refresh(stock)  # Ensure latest data is fetched
    return stock
