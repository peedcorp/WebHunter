#!/usr/bin/env python
# WebHunter MiniModule

import re


class Dancer:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(
                r'Dancer|dancer.session=*|',
                item[1],
                re.I) is not None
            if _:
                return "Dancer (Perl)"
                break
