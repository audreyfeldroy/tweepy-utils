# tweepy-utils

A set of Python utility scripts for Twitter account management, using [Tweepy](https://github.com/tweepy/tweepy).

## Installation

First the Twitter developer setup:

* Create a Twitter app at https://dev.twitter.com/apps.
* Grant your Twitter app read/write privileges.
* Create an access token.

Then install tweepy-utils from the Python Package Index:

    $ mkvirtualenv tweepy-utils
    $ pip install tweepy-utils
    $ mkdir tweepy-utils-data
    $ cd tweepy-utils-data
    $ cp config.ini.example config.ini

Finally open config.ini and add:

* Your Twitter username
* API key/secret
* Access token/secret

## Usage

List people who don't follow back:

    $ list-nonfollowers.py

Unfollow people who don't follow back:

    $ unfollow-nonfollowers.py

## Advanced Configuration

If you have multiple Twitter accounts, create a `your-twitter-username.ini` file for each account.

Then use the -c argument to run a script with a particular .ini file:

    $ list-nonfollowers.py -c your-twitter-username.ini
    $ unfollow-nonfollowers.py -c your-twitter-username.ini


## Credits

* list-nonfollowers.py and unfollow-nonfollowers.py are based on [Jamieson Becker's unfollow script](http://pastebin.com/CxUDMtMi)
