#!/usr/bin/env python
# WebHunter MiniModule

import re


class Netcontinuum:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'NCI__SessionId=', item[1], re.I) is not None
            if w:
                return "NetContinuum Web Application Firewall (NetContinuum/Barracuda Networks)"
                break
