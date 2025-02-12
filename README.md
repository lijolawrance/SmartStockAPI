# 📌 SmartStockAPI

**SmartStockAPI** is a **FastAPI-based stock tracking API** that **fetches real-time stock prices, stores historical data, and automates updates using Celery and Redis.**  

---

## 🚀 Features
✅ **Fetch Stock Prices** – Get live stock prices from FMP Cloud  
✅ **Historical Data Storage** – Each fetch inserts a new record (no updates)  
✅ **Automated Updates** – Celery schedules automatic stock updates  
✅ **Dockerized Services** – PostgreSQL, Redis, FastAPI, Celery in a seamless setup  
✅ **Future Plans**: 🔒 Move to **HTTPS** & 🔄 Switch to **Angel One API**  

---

## 🛠️ Setup & Installation
### 🔹 Prerequisites
- **Python 3.8+**  
- **Docker & Docker Compose**  
- **Makefile** (for easy management)  

### 🔹 Clone the Repository
```bash
git clone https://github.com/yourusername/SmartStockAPI.git
cd SmartStockAPI
```

### 🔹 Create a Virtual Environment
```bash
make activate  # Creates and activates a virtual environment
```

### 🔹 Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 📦 Running the Project
### 1️⃣ Start All Services (FastAPI, Celery, Redis, PostgreSQL)
```bash
make start-all
```

### 2️⃣ Fetch Live Stock Data
```bash
curl -X 'GET' 'http://127.0.0.1:8000/stocks/AAPL'
```

### 3️⃣ Fetch Historical Stock Data
```bash
curl -X 'GET' 'http://127.0.0.1:8000/stocks/AAPL/history'
```

### 4️⃣ Stop All Services
```bash
make stop-all
```

---

## 🛠️ Environment Variables
Create a `.env` file and add:
```
FMP_CLOUD_API_KEY=your_api_key_here
DATABASE_URL=postgresql://admin:password@localhost:5432/stock_db
REDIS_URL=redis://localhost:6379/0
```

---

## ⚡ Automating Stock Updates
**Celery is used to schedule automatic stock price updates.**
```bash
make start-celery-worker
make start-celery-beat
```
To manually trigger an update:
```python
from app.tasks import update_stock_price
update_stock_price.delay("AAPL")
```

---

## 🔮 Roadmap
✔ **Current Implementation** – Stock fetching, automation, database storage  
🔜 **Upcoming Features**  
- 🔒 **Move to HTTPS** for secure API calls  
- 🔄 **Switch to Angel One API** for better regional support  
- 🛡️ **JWT Authentication** for API security  

---

## 🤝 Contributing
Pull requests are welcome! Please follow coding standards and best practices.  

---

## 📄 License
This project is licensed under the **MIT License**.  
