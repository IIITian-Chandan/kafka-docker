# Steps to deploy KAFKA server.

Clone the repo: 
[**IIITian-Chandan/kafka-docker**](https://github.com/IIITian-Chandan/kafka-docker.git)

Start a cluster:

    docker-compose up -d

Add more brokers:

    docker-compose scale kafka=3

Destroy a cluster:

    docker-compose stop
