# Set default shell to bash
SHELL := /bin/bash

# Start Redis if not running
start-redis:
	@echo "🔍 Checking Redis..."
	@if ! docker ps | grep -q "redis_broker"; then \
		echo "🚀 Starting Redis..."; \
		docker start redis_broker; \
	else \
		echo "✅ Redis is already running."; \
	fi

# Start PostgreSQL if not running
start-db:
	@echo "🔍 Checking PostgreSQL..."
	@if ! docker ps | grep -q "postgres_db"; then \
		echo "🚀 Starting PostgreSQL..."; \
		docker start postgres_db; \
	else \
		echo "✅ PostgreSQL is already running."; \
	fi

# Start Celery Worker
start-celery-worker:
	@echo "🔍 Checking Celery Worker..."
	@if ! pgrep -f "celery -A app.tasks worker" > /dev/null; then \
		echo "🚀 Starting Celery Worker..."; \
		nohup celery -A app.tasks worker --loglevel=info > celery_worker.log 2>&1 & \
	else \
		echo "✅ Celery Worker is already running."; \
	fi

# Start Celery Beat
start-celery-beat:
	@echo "🔍 Checking Celery Beat..."
	@if ! pgrep -f "celery -A app.celery_worker beat" > /dev/null; then \
		echo "🚀 Starting Celery Beat..."; \
		nohup celery -A app.celery_worker beat --loglevel=info > celery_beat.log 2>&1 & \
	else \
		echo "✅ Celery Beat is already running."; \
	fi

# Start FastAPI
start-fastapi:
	@echo "🔍 Checking FastAPI..."
	@if pgrep -f "uvicorn app.main:app" > /dev/null; then \
		echo "🛑 FastAPI is already running. Restarting..."; \
		pkill -f "uvicorn app.main:app"; \
		sleep 2; \
	fi
	echo "🚀 Starting FastAPI..."
	nohup uvicorn app.main:app --reload > fastapi.log 2>&1 &



# Start all services
start-all: start-redis start-db start-celery-worker start-celery-beat start-fastapi
	@echo "🎉 All services are up and running!"

# Stop all services
stop-all:
	@echo "🛑 Stopping all services..."
	@pkill -f "celery -A app.tasks worker" || true
	@pkill -f "celery -A app.celery_worker beat" || true
	@pkill -f "uvicorn app.main:app" || true
	@echo "✅ Stopped Celery Worker, Celery Beat, and FastAPI."
