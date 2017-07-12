import pika
import logging
import json

def submit(job):
	connection = pika.BlockingConnection(pika.ConnectionParameters(
	        host='localhost'))
	channel = connection.channel()


	channel.queue_declare(queue='task_queue')
	channel.basic_publish(exchange='',
	                      routing_key='task_queue',
	                      body=json.dumps(job))
	logging.info(" [x] Sent 'Job!'%s"% job)
	connection.close()

