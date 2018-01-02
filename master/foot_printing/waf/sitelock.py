#!/usr/bin/env python
# WebHunter MiniModule

import re


class Sitelock:
    @staticmethod
    def run(content):
        w = False
        w = re.search(r'SiteLock Incident ID', content, re.I) is not None
        if w:
            return "TrueShield Web Application Firewall (SiteLock)"
