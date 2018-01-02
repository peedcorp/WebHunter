#!/usr/bin/env python
# WebHunter MiniModule

import re


class Chinacache:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'Powered-By-ChinaCache', item[0], re.I) is not None
            if w:
                return "ChinaCache-CDN"
                break
