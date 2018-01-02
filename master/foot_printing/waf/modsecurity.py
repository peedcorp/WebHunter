#!/usr/bin/env python
# WebHunter MiniModule

import re


class Modsecurity:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'Mod_Security|NOYB', item[1], re.I) is not None
            if w:
                return "ModSecurity Web Application Firewall (Trustwave)"
                break
