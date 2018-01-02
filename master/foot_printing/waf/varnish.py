#!/usr/bin/env python
# WebHunter MiniModule

import re


class Varnish:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'X-Varnish', item[0], re.I) is not None
            w |= re.search(r'varnish*', item[1], re.I) is not None
            if w:
                return "Varnish FireWall (OWASP)"
                break
