#!/usr/bin/env python
# WebHunter MiniModule

import re


class Perl:
    @staticmethod
    def run(content, headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'\.pl$|\.cgi$', content) is not None
            if _:
                return "Perl"
                break
