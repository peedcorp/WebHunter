#!/usr/bin/env python
# WebHunter MiniModule

import re


class Knownsec:
    @staticmethod
    def run(content):
        w = False
        w = re.search(
            r"url\('/ks-waf-error\.png'\)",
            content,
            re.I) is not None
        if w:
            return "KS-WAF (Knownsec)"
