#!/usr/bin/env python
# WebHunter MiniModule

import re


class Radware:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'X-SL-CompState', item[0], re.I) is not None
            if w:
                return "AppWall Web Application Firewall (Radware)"
                break
