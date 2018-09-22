from __future__ import absolute_import
from test_celery.celery import app
import time

@app.task
def longtime_add(x, y):
    print('long time task begins')
    # sleep 15 seconds
    time.sleep(15)
    print('long time task finished')
    return x + y

@app.task
def subtract(x, y):
    print('subtract task begins')
    # sleep 15 seconds
    time.sleep(10)
    print('subtract task finished')
    return x - y

@app.task
def multiply(x, y):
    print('Multiply task begins')
    # sleep 15 seconds
    time.sleep(10)
    print('Multiply task finished')
    return x * y
