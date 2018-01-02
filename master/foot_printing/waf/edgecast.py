#!/usr/bin/env python
# WebHunter MiniModule

import re


class Edgecast:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'ECDF', item[1], re.I) is not None
            if w:
                return "EdgeCast Web Application Firewall (Verizon)"
                break
