# twytto
Data engineering project for crypto currency analysis based on tweets.

Data Ingestion ->

The data is consumed from twitter "tweets" using the twitter API.
The libraries used for this section were:
    tweepy: to easily consume data from twitter's API.
    kafka-python: to create a kafka producer and send the data to "crypto" topic.
