from __future__ import absolute_import
from celery import Celery

#creating instance of the celery where broker is broker_url (i.e rabbitmq) in format : -> transport://user:password@hostname:port/virtual_host a
# "transport" for rabbitmq is "amqp"
#first argument to Celery is project package name
#third argument backend is backend url and rpc means sending the results back as AMQP messages

app = Celery('test_celery',
             broker='amqp://shanty:shanty123@localhost/shanty_vhost',
             backend='rpc://',
             include=['test_celery.tasks'])
