#!/usr/bin/env python
# WebHunter MiniModule

import re


class Unix:
    @staticmethod
    def run(os):
        _ = False
        for item in os.items():
            _ = re.search(r'unix', str(item), re.I) is not None
            if _:
                return "Unix"
                break
