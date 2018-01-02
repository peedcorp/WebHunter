#!/usr/bin/env python
# WebHunter MiniModule

import re


class Bsd:
    @staticmethod
    def run(os):
        _ = False
        for item in os.items():
            _ = re.search(r'\S*BSD', str(item), re.I) is not None
            if _:
                return "BSD"
                break
