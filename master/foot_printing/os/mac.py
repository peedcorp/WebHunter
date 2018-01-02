#!/usr/bin/env python
# WebHunter MiniModule

import re


class Mac:
    @staticmethod
    def run(os):
        _ = False
        for item in os.items():
            _ = re.search(r'Mac|MacOS|MacOS\S*', str(item)) is not None
            if _:
                return "MacOS"
                break
