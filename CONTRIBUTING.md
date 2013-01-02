# Contributors

* Audrey Roy - January 1, 2013
* Daniel Greenfeld - January 1, 2013

## Additional Credits

* list-nonfollowers.py and unfollow-nonfollowers.py are based on [Jamieson Becker's unfollow script](http://pastebin.com/CxUDMtMi)

# How to Contribute

## Fork, Code, Send Pull Requests

* Fork this repository
* Send a pull request in a branch named for the feature

## Prefer Pull Requests

Got an idea or suggestion? Open a pull request rather than filing an issue, if you can.

## Setting up tweepy-utils for development

Do the following:

    $ git clone git@github.com:your-github-username/tweepy-utils.git
    $ cd tweepy-utils
    $ cp config.ini.example audreyr.ini
    $ mkvirtualenv tweepy-utils
    (tweepy-utils) $ python setup.py develop

Then run the scripts like this:

    (tweepy-utils) $ python scripts/list-nonfollowers.py -c audreyr.ini
    (tweepy-utils) $ python scripts/unfollow-nonfollowers.py -c audreyr.ini
