#!/usr/bin/env python
# WebHunter MiniModule

import re


class Baidu():
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'yunjiasu-nginx', item[1], re.I) is not None
            w |= re.search(r'YJS-ID', item[1], re.I) is not None
            w |= re.search(r'fhl', item[1], re.I) is not None
            if w:
                return "Yunjiasu Web Application Firewall (Baidu)"
                break
