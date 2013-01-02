from argparse import ArgumentParser
from ConfigParser import SafeConfigParser

argparser = ArgumentParser(description="Unfollow people who don't follow back.")
argparser.add_argument('-c', action='store', dest='config_file', default='config.ini')
args = argparser.parse_args()

confparser = SafeConfigParser()
confparser.read(str(args.config_file))

username = confparser.get('twitter_account', 'username')
consumer_key = confparser.get('twitter_account', 'consumer_key')
consumer_secret = confparser.get('twitter_account', 'consumer_secret')
access_token = confparser.get('twitter_account', 'access_token')
access_token_secret = confparser.get('twitter_account', 'access_token_secret')
