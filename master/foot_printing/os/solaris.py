#!/usr/bin/env python
# WebHunter MiniModule

import re


class Solaris:
    @staticmethod
    def run(os):
        _ = False
        for item in os.items():
            _ = re.search(
                r'solaris|sunos|opensolaris|sparc64|sparc',
                str(item),
                re.I) is not None
            if _:
                return "Solaris"
                break
