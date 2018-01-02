#!/usr/bin/env python
# WebHunter MiniModule

import re


class Ruby:
    @staticmethod
    def run(content, headers):
        _ = False
        for item in headers.items():
            _ = re.search(
                r"mod_rack|phusion|passenger",
                item[1],
                re.I) is not None
            _ |= re.search(r'\.rb$|\.rhtml$', content) is not None
            if _:
                return "Ruby"
                break
