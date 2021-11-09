from kafka import KafkaConsumer
from json import loads
from pymongo import MongoClient

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'crypto',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='latest',
        enable_auto_commit=True)

    client = MongoClient('localhost:27017')
    collection = client.twytto.crypto

    for message in consumer:
        message = message.value.decode('utf-8')
        collection.insert_one(loads(message))
        print('{} added to {}'.format(message, collection))