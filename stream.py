#!/usr/bin/env python

#-----------------------------------------------------------------------
# twitter-stream-format:
#  - ultra-real-time stream of twitter's public timeline.
#    does some fancy output formatting.
#-----------------------------------------------------------------------

from twitter import *
import re
import datetime
from datetime import timedelta


#-----------------------------------------------------------------------
# import a load of external features, for text display and date handling
# you will need the termcolor module:
#
# pip install termcolor
#-----------------------------------------------------------------------
from time import strftime
from textwrap import fill
from termcolor import colored
from email.utils import parsedate

#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
import sys
sys.path.append(".")
import config

#-----------------------------------------------------------------------
# create twitter streaming API object
#-----------------------------------------------------------------------
def create_stream():
    myAuth = OAuth(config.access_key,
                config.access_secret,
                config.consumer_key,
                config.consumer_secret)
    twitter_stream = TwitterStream(auth = myAuth, secure = True)
    return twitter_stream

#-----------------------------------------------------------------------
# iterate over tweets matching this filter text
#-----------------------------------------------------------------------


# while datetime.datetime.now() != future:
def get_stream(twitter_stream):
    date_time = datetime.datetime.now()
    future = date_time + timedelta(minutes=10)
    # later = future.strftime("%H:%M:%S")
    tweet_buff = []

    iterator = twitter_stream.statuses.sample()

    for tweet in iterator:
        tweet_buff.append(tweet)
        if datetime.datetime.now() > future:
            return tweet_buff, date_time, future
