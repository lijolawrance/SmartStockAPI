from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database, crud, services
from app.schemas import StockResponse
from app.database import engine
from app import models

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/stocks/{symbol}", response_model=StockResponse)
def fetch_and_store_stock(symbol: str, db: Session = Depends(database.get_db)):
    """Fetch full stock data from API, store it, and return the response"""
    stock_data = services.fetch_stock_price(symbol)

    if not stock_data:
        raise HTTPException(status_code=404, detail="Stock data not available")

    stock = crud.add_stock(db, stock_data)

    if not stock:
        raise HTTPException(status_code=500, detail="Stock could not be stored")

    return stock
