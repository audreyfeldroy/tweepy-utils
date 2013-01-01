#! /usr/bin/env python

# Based on Jamieson Becker's unfollow script http://pastebin.com/CxUDMtMi

import time
import tweepy
import sys

from argparse import ArgumentParser
from ConfigParser import SafeConfigParser

argparser = ArgumentParser(description="Unfollow people who don't follow back.")
argparser.add_argument('-c', action='store', dest='config', default='config')
args = argparser.parse_args()
print args

config_file = "%s.ini" % args.config
print config_file
confparser = SafeConfigParser()
confparser.read(str(config_file))

consumer_key = confparser.get('twitter_account', 'consumer_key')
consumer_secret = confparser.get('twitter_account', 'consumer_secret')
access_token = confparser.get('twitter_account', 'access_token')
access_token_secret = confparser.get('twitter_account', 'access_token_secret')

auth = tweepy.auth.OAuthHandler(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret)
auth.set_access_token(
        access_token,
        access_token_secret)

# the following dictionaries etc aren't strictly needed for this
# but useful for your own more in-depth apps.


api = tweepy.API(auth_handler=auth)

print "Loading followers.."
followers = []
for follower in tweepy.Cursor(api.followers).items():
    followers.append(follower)

print "Found %s followers, finding friends.." % len(followers)
friends = []
for friend in tweepy.Cursor(api.friends).items():
    friends.append(friend)

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

print "Unfollowing %s people who don't follow you back" % len(non_friends)
print "This will take approximately %s minutes." % (len(non_friends) / 60.0)
answer = raw_input("Are you sure? [Y/n]").lower()
if answer and answer[0] != "y":
    sys.exit(1)

# actually start the removal process. In the event of a failure (thanks,
# twitter), retry once after five seconds. An error on same record again
# is probably more serious issue, exit and error occurs

for nf in non_friends:
    print "Unfollowing %s" % nf.screen_name
    try:
        nf.unfollow()
    except:
        print "  .. failed, sleeping for 5 seconds and then trying again."
        time.sleep(5)
        nf.unfollow()
    print " .. completed, sleeping for 1 second."
    time.sleep(1)
