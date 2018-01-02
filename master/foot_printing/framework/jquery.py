#!/usr/bin/env python
# WebHunter MiniModule

import re


class Jquery:
    @staticmethod
    def run(content):
        _ = False
        _ = re.search(r'jquery\.js|jquery\.min\.js', content, re.I) is not None
        _ |= re.search(r'jquery-migrate\.min\.js', content, re.I) is not None
        if _:
            return "Jquery"
