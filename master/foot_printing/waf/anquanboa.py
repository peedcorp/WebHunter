#!/usr/bin/env python
# WebHunter MiniModule

import re


class Anquanboa:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'X-Powered-By-Anquanbao', item[0], re.I) is not None
            if w:
                return "Anquanbao Firewall"
                break
