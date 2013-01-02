from distutils.core import setup

setup(
    name='tweepy-utils',
    version='0.1dev7',
    description='A set of Python utility scripts for Twitter account management, using Tweepy.',
    author='Audrey Roy',
    author_email='audreyr@cartwheelweb.com',
    url='https://github.com/audreyr/tweepy-utils/',
    license='MIT license',
    install_requires=[
        'tweepy == 1.12',
    ],
    scripts=[
        'scripts/list-nonfollowers.py',
        'scripts/unfollow-nonfollowers.py'
    ],
)
