#!/usr/bin/env python
# WebHunter MiniModule

import re


class Safedog:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'WAF/2\.0', item[1], re.I) is not None
            w |= re.search(r'Safedog', item[1], re.I) is not None
            if w:
                return "Safedog Web Application Firewall (Safedog)"
                break
