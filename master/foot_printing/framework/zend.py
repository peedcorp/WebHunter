#!/usr/bin/env python
# WebHunter MiniModule

import re


class Zend:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'Zend', item[1], re.I) is not None
            if _:
                return "Zend (PHP)"
                break
