#!/usr/bin/env python
# WebHunter MiniModule

import re


class Bigip():
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'BigIP|BIGipServer', item[1], re.I) is not None
            w |= re.search(r'TS\w{4,}=', item[1], re.I) is not None
            w |= re.search(r'F5', item[1], re.I) is not None
            if w:
                return "BIG-IP Application Security Manager (F5 Networks)"
                break
