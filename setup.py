#!/usr/bin/env python
from setuptools import setup

setup(
    name='scrapy-streaming',
    version='0.1',
    url='https://github.com/scrapy-plugins/scrapy-streaming',
    description='Develop Spiders using any Programming Language',
    author='Scrapy developers',
    packages=['scrapy_streaming'],
    requires=['scrapy'],

    entry_points={
        'scrapy.commands': [
            'streaming=scrapy_streaming.commands.streaming:StreamingCommand',
            'list=scrapy_streaming.commands.list:ListCommand',
            'crawl=scrapy_streaming.commands.crawl:CrawlCommand'
        ],
    },
)
