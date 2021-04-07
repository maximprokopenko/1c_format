from setuptools import setup, find_packages
from os.path import join, dirname


AUTHOR = "Maxim Prokopenko"
AUTHOR_EMAIL = "maximprokopenko@gmail.com"
NAME = "1c_format"
PACKAGE = '1c_format'
VERSION = '0.1'
URL = 'https://github.com/maximprokopenko/1c_format'


setup(
    name=NAME,
    packages=[PACKAGE],
    version=VERSION,
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=[]
)
