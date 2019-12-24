import requests
from time import sleep


from kafka import KafkaProducer
from kq import Queue

# Set up a Kafka producer.
producer = KafkaProducer(bootstrap_servers='34.67.1.98:9092')

# Set up a queue.
queue = Queue(topic='topic_queue', producer=producer)

# Enqueue a function call.
job = queue.enqueue(requests.get, 'https://www.google.com')
sleep(.1)
print("success")


