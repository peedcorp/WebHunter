#!/usr/bin/env python
# WebHunter MiniModule

import re


class Jiasule:
    @staticmethod
    def run(content, headers):
        w = False
        for item in headers.items():
            w = re.search(r"jiasule-WAF", item[1], re.I) is not None
            w |= re.search(r"__jsluid=", item[1], re.I) is not None
            w |= re.search(
                r"static\.jiasule\.com/static/js/http_error\.js",
                content,
                re.I) is not None
            if w:
                return "Jiasule Web Application Firewall (Jiasule)"
                break
