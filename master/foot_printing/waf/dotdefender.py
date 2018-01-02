#!/usr/bin/env python
# WebHunter MiniModule

import re


class Dotdefender:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'X-dotDefender-denied', item[0], re.I) is not None
            if w:
                return "dotDefender Web Application Firewall (Applicure Technologies)"
                break
