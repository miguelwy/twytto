# Twytto
## Big Data Real-time Crypto Analysis
**Data engineering project for crypto currency analysis using twitter API.** <br />

![alt text](images/fluxo.png)

For this project to work you'll have to configure the following: <br />
    - **Zookeeper** running on port 2181. <br />
    - **Apache Kafka** running on port 9092. <br />
    - Create topic **"crypto"** on apache kafka's cluster. <br />
    - **MongoDb** instance running on port 27017 <br />
    - **Twitter developer** account (API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET) <br />

### Data Streaming <br />

The data is consumed from twitter "tweets" using the twitter API. The code can be found on "producer.py" file. <br />
<br />
The libraries used for this section were: <br />
    - **tweepy**: to easily consume data stream from twitter's API. <br />
    - **kafka-python**: to create a kafka producer and send the data to "crypto" topic. <br />
    
### Data Consuming and Persistency <br />

In this part, a kafka consumer listens to the "crypto" topic and inserts all messages into a collection inside MongoDb instance. The code can be found on "consumer.py" file. <br />
<br />
The libraries used for this section were: <br />
    - **pymongo**: to easily work with mongodb <br />
    - **kafka-python**: to create the kafka consumer and listen to "crypto" topic. <br />
