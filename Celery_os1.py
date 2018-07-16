

# -*- coding: utf-8 -*-
from celery import Celery
from celery.schedules import crontab

broker = 'redis://127.0.0.1:6379/0'
backend = 'redis://127.0.0.1:6379/1'

app = Celery('tasks',  broker=broker, backend=backend)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s(x='111',y='2222'), name='add every 10')

@app.task
def test(x,y):
    print("running...",x,y)
