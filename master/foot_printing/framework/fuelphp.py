#!/usr/bin/env python
# WebHunter MiniModule

import re


class Fuelphp:
    @staticmethod
    def run(headers, content):
        _ = False
        for item in headers.items():
            _ = re.search(r'fuelcid=', item[1], re.I) is not None
            _ |= re.search(
                r'Powered by <a href="http://fuelphp.com">FuelPHP</a>',
                content) is not None
            if _:
                return "FuelPHP (PHP)"
                break
