#!/usr/bin/env python
# WebHunter MiniModule

import re


class Urlscan:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'Rejected-By-UrlScan', item[0], re.I) is not None
            if w:
                return "UrlScan Firewall (Microsoft)"
                break
