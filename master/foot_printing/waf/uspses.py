#!/usr/bin/env python
# WebHunter MiniModule

import re


class Uspses:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r"Secure Entry Server", item[1], re.I) is not None
            if w:
                return "USP Secure Entry Server (United Security Providers)"
                break
