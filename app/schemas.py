from pydantic import BaseModel
from datetime import datetime

class StockResponse(BaseModel):
    id: int  # Added ID field
    symbol: str
    name: str
    price: float
    changes_percentage: float
    change: float
    day_low: float
    day_high: float
    year_high: float
    year_low: float
    market_cap: int
    price_avg_50: float
    price_avg_200: float
    exchange: str
    volume: int
    avg_volume: int
    open_price: float
    previous_close: float
    eps: float
    pe: float
    earnings_announcement: str
    shares_outstanding: int
    timestamp: datetime  # Changed to datetime for correct formatting

    class Config:
        orm_mode = True  # Allows Pydantic to work with SQLAlchemy models
