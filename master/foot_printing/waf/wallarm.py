#!/usr/bin/env python
# WebHunter MiniModule

import re


class Wallarm():
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'nginx-wallarm', item[1], re.I) is not None
            if w:
                return "Wallarm Web Application Firewall (Wallarm)"
                break
