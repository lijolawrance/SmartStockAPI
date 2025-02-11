from sqlalchemy import Column, String, Float, BigInteger, DateTime
from app.database import Base
import datetime

class Stock(Base):
    __tablename__ = "stocks"

    symbol = Column(String, primary_key=True)
    name = Column(String)
    price = Column(Float)
    changes_percentage = Column(Float)
    change = Column(Float)
    day_low = Column(Float)
    day_high = Column(Float)
    year_high = Column(Float)
    year_low = Column(Float)
    market_cap = Column(BigInteger)
    price_avg_50 = Column(Float)
    price_avg_200 = Column(Float)
    exchange = Column(String)
    volume = Column(BigInteger)
    avg_volume = Column(BigInteger)
    open_price = Column(Float)
    previous_close = Column(Float)
    eps = Column(Float)
    pe = Column(Float)
    earnings_announcement = Column(String)
    shares_outstanding = Column(BigInteger)
    timestamp = Column(BigInteger, default=datetime.datetime.utcnow)
