from sqlalchemy import Column, String, Float, BigInteger, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(
        BigInteger, primary_key=True, autoincrement=True
    )  # Unique ID for each record
    symbol = Column(
        String, nullable=False, index=True
    )  # Stock ticker symbol (e.g., AAPL, TSLA)
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
    timestamp = Column(
        DateTime, default=datetime.datetime.utcnow, index=True
    )  # Auto-set timestamp
