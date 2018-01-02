#!/usr/bin/env python
# WebHunter MiniModule

import re


class Sucuri:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'Sucuri|Cloudproxy', item[1], re.I) is not None
            w |= re.search(r'X-Sucuri-ID', item[0], re.I) is not None
            if w:
                return "CloudProxy WebSite Firewall (Sucuri)"
                break
