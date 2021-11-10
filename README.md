![](https://img.shields.io/badge/python-3.9.5-green)
![](https://img.shields.io/badge/zookeeper-3.7.0-green)
![](https://img.shields.io/badge/apache--kafka-2.4.1-green)
# Twyto
## Big Data Real-time Crypto Analysis
**Data engineering project for crypto currency analysis using twitter API.** <br />

![alt text](images/fluxograma.png)

For this project to work you'll have to configure the following: <br />
    - **Zookeeper** <br />
    - **Apache Kafka**<br />
    - **MongoDb**<br />
    - **Twitter developer** account (API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET) <br />

You can specify the ports, servers and other configurations using the **config.py** file. Please note that all parameters are mandatory for this project to work. <br />

### Data Streaming <br />

The data is consumed from twitter "tweets" using the twitter API. The code can be found on "producer.py" file. <br />
<br />
The libraries used for this section were: <br />
    - **tweepy**: to easily consume data stream from twitter's API. <br />
    - **kafka-python**: to create a kafka producer and send the data to the specified kafka topic. <br />
    
### Data Consuming and Persistency <br />

In this part, a kafka consumer listens to the specified kafka topic and inserts all messages into a collection inside MongoDb instance. The code can be found on "consumer.py" file. <br />
<br />
The libraries used for this section were: <br />
    - **pymongo**: to easily work with mongodb <br />
    - **kafka-python**: to create the kafka consumer and listen to the specified topic. <br />
    
### Running <br />

- Run zookeeper server
- Run kafka cluster
- Inside "data-consumer" folder run "consumer.py"
- Inside "data-stream" folder run "producer.py"

