#!/usr/bin/env python
# WebHunter MiniModule

import requests
from agent import usage


class request():
    def __init__(self, url):
        self.agent = usage()
        self.url = url
        self.client = requests.session()
        self.client.headers = {'User-Agent': self.agent}
        self.response = self.client.get(self.url, allow_redirects=False)
        self.content = self.response.content
        self.status_code = self.response.status_code
