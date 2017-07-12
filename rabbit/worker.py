#!/usr/bin/env python
import pika
import time
import threading

def workerrmq():

	connection = pika.BlockingConnection(pika.ConnectionParameters(
		host='localhost'))
	channel = connection.channel()

	channel.queue_declare(queue='hello')
	print(' [*] Waiting for messages. To exit press CTRL+C')
	channel.basic_qos(prefetch_count=1)
	channel.basic_consume(callback,
			      queue='hello')
	channel.start_consuming()

def callback(ch, method, properties, body):
	    print(" [x] Received %r" % body)
	    time.sleep(1)
	    print(" [x] Done")
	    ch.basic_ack(delivery_tag = method.delivery_tag)



threads = []
for i in range(3):
	    t = threading.Thread(target=workerrmq)
	    threads.append(t)
	    t.start()
