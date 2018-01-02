#!/usr/bin/env python
# WebHunter MiniModule

import re


class Django:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'csrftoken=', item[1], re.I) is not None
            if _:
                return "Django (Python)"
                break
