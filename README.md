tweepy-utils
============

A set of Python utility scripts for Twitter account management, using Tweepy.

Installation
------------

For now:

    $ mkvirtualenv tweepy-utils
    $ pip install tweepy
    $ git clone ...
    $ cd tweepy-utils
    $ cp config.ini.example config.ini

Then open config.ini and add your Twitter username and API key/secret.

Usage
-----

List people who don't follow back:

    $ python list-nonfollowers.py

Unfollow people who don't follow back:

    $ python unfollow-nonfollowers.py

Credits
-------

* unfollow-nonfollowers.py is based on [Jamieson Becker's unfollow script](http://pastebin.com/CxUDMtMi)
