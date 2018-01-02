#!/usr/bin/env python
# WebHunter MiniModule

import re


class Fortiweb:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'FORTIWAFSID=', item[1], re.I) is not None
            if w:
                return "FortiWeb Web Application Firewall (Fortinet)"
                break
