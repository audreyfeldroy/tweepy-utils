#! /usr/bin/env python

# Based on Jamieson Becker's unfollow script http://pastebin.com/CxUDMtMi

import time
import tweepy
import sys

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')

username = parser.get('twitter_account', 'username')
consumer_key = parser.get('twitter_account', 'consumer_key')
consumer_secret = parser.get('twitter_account', 'consumer_secret')
access_token = parser.get('twitter_account', 'access_token')
access_token_secret = parser.get('twitter_account', 'access_token_secret')

auth = tweepy.auth.OAuthHandler(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret)
auth.set_access_token(
        access_token,
        access_token_secret)

# the following dictionaries etc aren't strictly needed for this
# but useful for your own more in-depth apps.


api=tweepy.API(auth_handler=auth)

followers = []
for follower in tweepy.Cursor(api.followers).items():
    followers.append(follower)

friends = []
for friend in tweepy.Cursor(api.friends).items():
    friends.append(friend)

print "Stats for %s:" % username
print "%d following" % len(friends)
print "%d followers" % len(followers)
print "..."

# creating dictionaries based on id's is handy too

friend_dict = {}
for friend in friends:
    friend_dict[friend.id] = friend

follower_dict = {}
for follower in followers:
    follower_dict[follower.id] = follower

# now we find all your "non_friends" - people who don't follow you
# even though you follow them.

non_friends = [friend for friend in friends if friend.id not in follower_dict]

# double check, since this could be a rather traumatic operation.

print "Here are the %s people who don't follow you back" % len(non_friends)

# actually start the removal process. In the event of a failure (thanks,
# twitter), retry once after five seconds. An error on same record again
# is probably more serious issue, exit and error occurs

for nf in non_friends:
    print nf.screen_name
