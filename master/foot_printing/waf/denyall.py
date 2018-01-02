#!/usr/bin/env python
# WebHunter MiniModule

import re


class Denyall:
    @staticmethod
    def run(content, code, headers):
        w = False
        for item in headers.items():
            w = re.search(r"\Asessioncookie=", item[1], re.I) is not None
            w |= code == 200 and re.search(
                r"\ACondition Intercepted", content, re.I) is not None
            if w:
                return "Deny All Web Application Firewall (DenyAll)"
                break
