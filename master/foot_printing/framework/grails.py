#!/usr/bin/env python
# WebHunter MiniModule

import re


class Grails:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'Grails', item[1], re.I) is not None
            _ |= re.search(
                r'X-Grails|X-Grails-Cached',
                item[0],
                re.I) is not None
            if _:
                return "Grails (Java)"
                break
