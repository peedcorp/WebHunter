#!/usr/bin/env python
# WebHunter MiniModule

import re


class Barracuda():
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'barracuda*', item[1], re.I) is not None
            w |= re.search(
                r'barra_counter_session=',
                item[1],
                re.I) is not None
            w |= re.search(r'barracuda_', item[1], re.I) is not None
            if w:
                return "Barracuda Web Application Firewall (Barracuda Networks)"
                break
