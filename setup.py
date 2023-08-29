from setuptools import setup, find_packages

setup(
    name='tweepy-utils',
    version='0.1dev7',
    description='A set of Python utility scripts for Twitter account management, using Tweepy.',
    author='Audrey Roy',
    author_email='audreyr@cartwheelweb.com',
    url='https://github.com/audreyr/tweepy-utils/',
    license='MIT license',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'tweepy==3.0',
    ],
    packages=find_packages(),
    scripts=[
        'scripts/list-nonfollowers.py',
        'scripts/unfollow-nonfollowers.py'
    ],
)
