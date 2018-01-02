#!/usr/bin/env python
# WebHunter MiniModule

import re


class Webknight():
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'Webknight', item[1], re.I) is not None
            if w:
                return "WebKnight Application Firewall (AQTRONIX)"
                break
