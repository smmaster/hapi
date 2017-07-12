#!/usr/bin/env python
import pika
import time
from multiprocessing import Pool
import concurrent.futures


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
	    time.sleep(10)
	    print(" [x] Done")
	    ch.basic_ack(delivery_tag = method.delivery_tag)



if __name__ == '__main__':
   with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
      for n in range(10):
         executor.submit(workerrmq)
