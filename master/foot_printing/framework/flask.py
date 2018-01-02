#!/usr/bin/env python
# WebHunter MiniModule

import re


class Flask:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'flask', item[1], re.I) is not None
            if _:
                return "Flask (Python)"
                break
