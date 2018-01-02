#!/usr/bin/env python
# WebHunter MiniModule

import re


class Windows:
    @staticmethod
    def run(os):
        _ = False
        for item in os.items():
            _ = re.search(r'windows|win32', str(item), re.I) is not None
            if _:
                return "Windows"
                break
