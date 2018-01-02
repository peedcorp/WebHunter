#!/usr/bin/env python
# WebHunter MiniModule

import re


class Teros:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r"\Ast8(id|_wat|_wlf)", item[1], re.I) is not None
            if w:
                return "Teros/Citrix Application Firewall Enterprise (Teros/Citrix Systems)"
                break
