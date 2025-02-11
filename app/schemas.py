from pydantic import BaseModel

class StockResponse(BaseModel):
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
    timestamp: int

    class Config:
        orm_mode = True
