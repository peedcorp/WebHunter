#!/usr/bin/env python
# WebHunter MiniModule

import re


class Paloalto:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'MISS from PaloAlto', item[1], re.I) is not None
            if w:
                return "Palo Alto Firewall (Palo Alto Networks)"
                break
