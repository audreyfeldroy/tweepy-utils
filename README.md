tweepy-utils
============

A set of Python utility scripts for Twitter account management, using Tweepy.

Installation
------------

First the Twitter developer setup:

* Create a Twitter app at https://dev.twitter.com/apps.
* Grant your Twitter app read/write privileges.
* Create an access token.

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

Unfollow people who don't follow back, using the settings from pcs.ini:

    $ python unfollow-nonfollowers.py -c pcs

Credits
-------

* unfollow-nonfollowers.py is based on [Jamieson Becker's unfollow script](http://pastebin.com/CxUDMtMi)
