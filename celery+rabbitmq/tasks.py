from celery import Celery

app = Celery(__name__, broker='amqp://guest:guest@localhost:5672//')

@app.task
def add(x, y):   
        return x + y