#!/usr/bin/env python
# WebHunter MiniModule

import re


class Cloudflare:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'cloudflare[-nginx]', item[1], re.I) is not None
            w |= re.search(r'__cfduid=', item[1], re.I) is not None
            w |= re.search(r'cf-ray', item[0], re.I) is not None
            if w:
                return "CloudFlare Web Application Firewall (CloudFlare)"
                break
