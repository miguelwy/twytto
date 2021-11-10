import tweepy
from keys import *
from kafka import KafkaProducer

class MaxStream(tweepy.Stream):

    def on_data(self,raw_data):
        self.process_data(raw_data)
        return True

    def process_data(self, raw_data):
        producer.send("crypto", raw_data)
        print(raw_data)

    def on_error(self, status_code):
        if status_code == 420:
            return False

    def start(self):
        self.filter(track=["bitcoin"],filter_level='low')

if __name__ == '__main__':
    
    producer = KafkaProducer(bootstrap_servers='localhost:9092')

    stream = MaxStream( API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    stream.start()
