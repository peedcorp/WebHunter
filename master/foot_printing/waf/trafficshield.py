#!/usr/bin/env python
# WebHunter MiniModule

import re


class Trafficshield:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'F5-TrafficShield', item[1], re.I) is not None
            w |= re.search(r'ASINFO=', item[1], re.I) is not None
            if w:
                return "TrafficShield (F5 Networks)"
                break
