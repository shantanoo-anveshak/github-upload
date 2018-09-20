from __future__ import absolute_import
from test_celery.celery import app
import time


@app.task
def longtime_add(x, y):
    print('long time task begins')
    # sleep 10 seconds
    time.sleep(10)
    print('long time task finished')
    return x + y
