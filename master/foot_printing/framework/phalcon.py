#!/usr/bin/env python
# WebHunter MiniModule

import re


class Phalcon:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'phalcon-auth-*', item[1], re.I) is not None
            _ |= re.search(
                r'Phalcon [(https://phalconphp.com/)]*',
                item[1]) is not None
            if _:
                return "Phalcon (C and PHP)"
                break
