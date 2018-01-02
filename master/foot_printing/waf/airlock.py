#!/usr/bin/env python
# WebHunter MiniModule

import re


class Airlock:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'^AL[_-]SESS[_-]S=\S*', item[1], re.I) is not None
            w |= re.search(r'X-Airlock-Test', item[0], re.I) is not None
            if w:
                return "InfoGuard Airlock (Phion/Ergon)"
                break
