from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://admin:password@localhost:5432/stock_db"

engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20, pool_timeout=30, pool_recycle=1800)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# ✅ Function to get database session
def get_db():
    """Provides a new database session for each request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # Ensure the session is closed after use
