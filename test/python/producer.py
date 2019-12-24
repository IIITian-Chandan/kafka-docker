from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['34.67.1.98:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for e in range(10):
    data = {
        "db_collection_name": "chandan_test",
        "env": "testing",
        "html_text": "<html><head>\n<title>Access Denied</title>\n</head><body>\n<h1>Access Denied</h1>\n \nYou don't have permission to access \"http://www.asos.com/men/\" on this server.<p>\nReference #18.2e4fc817.1557899946.936020da\n\n\n</p></body></html>",
        "kafka_topic": "thunder_testing",
        "url": "https://www.asos.com/men/"
    }

    producer.send('kafka_testing', value=data)
    print("take")
    sleep(5)
