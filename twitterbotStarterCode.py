#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
import random
 
class TwitterAPI:
    def __init__(self):
        consumer_key = ""
        consumer_secret = ""
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = ""
        access_token_secret = ""
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
 
    def tweet(self, message):
        self.api.update_status(status=message)
 
if __name__ == "__main__":
    filename=open('gamelan.txt','r')
    f=filename.readlines()
    filename.close()
    twitter = TwitterAPI()
    twitter.tweet(random.choice(f))