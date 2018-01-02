#!/usr/bin/env python
# WebHunter MiniModule

import re


class Incapsula:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(
                r'incap_ses|visid_incap|Incapsula',
                item[1],
                re.I) is not None
            if w:
                return "Incapsula Web Application Firewall (Incapsula/Imperva)"
                break
