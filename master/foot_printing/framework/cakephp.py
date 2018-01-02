#!/usr/bin/env python
# WebHunter MiniModule

import re


class Cakephp:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'cakephp=', item[1], re.I) is not None
            if _:
                return "CakePHP (PHP)"
                break
