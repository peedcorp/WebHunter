#!/usr/bin/env python
# WebHunter MiniModule

import re


class Profense:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'PLBSID=', item[1], re.I) is not None
            w = re.search(r'Profense', item[1], re.I) is not None
            if w:
                return "Profense Web Application Firewall (Armorlogic)"
                break
