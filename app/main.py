from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database, crud, services
from app.schemas import StockResponse
from app.database import engine, get_db
from app import models

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/stocks/{symbol}", response_model=StockResponse)
def fetch_and_store_stock(
    symbol: str, db: Session = Depends(get_db)
):  # ✅ Use get_db instead of database.get_db
    """Fetch full stock data from API, store it as a new record, and return the latest"""
    stock_data = services.fetch_stock_price(symbol)

    if not stock_data:
        raise HTTPException(status_code=404, detail="Stock data not available")

    # Insert new stock record every time
    crud.insert_stock(db, stock_data)

    # Return the latest record
    latest_stock = crud.get_latest_stock(db, symbol)

    if not latest_stock:
        raise HTTPException(status_code=500, detail="Stock could not be retrieved")

    return latest_stock


@app.get("/stocks/{symbol}/history", response_model=list[StockResponse])
def get_stock_history(
    symbol: str, limit: int = 10, db: Session = Depends(database.get_db)
):
    """Fetch the historical stock data for a given symbol"""
    stock_history = crud.get_stock_history(db, symbol, limit)

    if not stock_history:
        raise HTTPException(status_code=404, detail="Stock history not available")

    return stock_history
