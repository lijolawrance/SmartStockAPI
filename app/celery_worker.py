from celery import Celery
import os
from celery.schedules import crontab


# Celery configuration
celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",  # Redis URL
    backend="redis://localhost:6379/0"  # Redis used as result backend
)

celery.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
)

celery.conf.beat_schedule = {
    "update_aapl_every_minute": {
        "task": "app.tasks.update_stock_price",
        "schedule": crontab(minute="*/1"),  # Every 1 minute
        "args": ("AAPL",),
    },
    "update_tsla_every_five_minutes": {
        "task": "app.tasks.update_stock_price",
        "schedule": crontab(minute="*/5"),  # Every 5 minutes
        "args": ("TSLA",),
    },
}