from kafka import KafkaConsumer
from json import loads
from time import sleep
import json

consumer = KafkaConsumer(bootstrap_servers='34.67.1.98:9092',
                         auto_offset_reset='earliest',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
consumer.subscribe(['thunder_testing'])
for message in consumer:
    print()
    message = message.value
    print(message)
    sleep(0.1)
