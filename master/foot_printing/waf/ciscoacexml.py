#!/usr/bin/env python
# WebHunter MiniModule

import re


class Ciscoacexml:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'ACE XML Gateway', item[1], re.I) is not None
            if w:
                return "Cisco ACE XML Gateway (Cisco Systems)"
                break
