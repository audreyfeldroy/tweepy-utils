tweepy-utils
============

A set of Python utility scripts for Twitter account management, using Tweepy.

Installation
------------

First the Twitter developer setup:

* Create a Twitter app at https://dev.twitter.com/apps.
* Create an access token.
* Grant your Twitter app read/write privileges.

Then (for now):

    $ mkvirtualenv tweepy-utils
    $ pip install -r requirements.txt
    $ git clone ...
    $ cd tweepy-utils
    $ cp config.ini.example config.ini

Finally open config.ini and add:

* Your Twitter username
* API key/secret
* Access token/secret

Usage
-----

List people who don't follow back:

    $ python list-nonfollowers.py

Unfollow people who don't follow back:

    $ python unfollow-nonfollowers.py

Credits
-------

* unfollow-nonfollowers.py is based on [Jamieson Becker's unfollow script](http://pastebin.com/CxUDMtMi)
