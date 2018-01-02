#!/usr/bin/env python
# WebHunter MiniModule

import re


class Nette:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'nette*|nette-browser=*', item[1], re.I) is not None
            if _:
                return "Nette (PHP)"
                break
