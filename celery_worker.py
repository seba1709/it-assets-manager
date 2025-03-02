from celery import Celery
import os

app = Celery(
    'tasks',
    broker=os.getenv("REDIS_URL", "redis://localhost:6379/0"),
    backend=os.getenv("REDIS_URL", "redis://localhost:6379/0")
)

@app.task
def test_task():
    return "Celery is working!"

