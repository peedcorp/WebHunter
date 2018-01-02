#!/usr/bin/env python
# WebHunter MiniModule

import re


class Binarysec():
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'BinarySec', item[1], re.I) is not None
            w |= re.search(
                r'x-binarysec-[via|nocahe]',
                item[0],
                re.I) is not None
            if w:
                return "BinarySEC Web Application Firewall (BinarySEC)"
                break
