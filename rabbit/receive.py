#!/usr/bin/env python
import pika
import time
import threading
import logging


def worker():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')

def callback(ch, method, properties, body):
        logging.info(" [x] Received %r" % body) 
        time.sleep(1)
        logging.info(" [x] END ") 
        ch.basic_ack(delivery_tag = method.delivery_tag)


def workerrmq():

        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='task_queue')

        logging.info(' [*] Waiting for messages. To exit press CTRL+C')
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(callback,
                      queue='task_queue')

        channel.start_consuming()


   

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)

threads = []
for i in range(3):
    t = threading.Thread(target=workerrmq)
    threads.append(t)
    t.start()


