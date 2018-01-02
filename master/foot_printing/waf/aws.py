#!/usr/bin/env python
# WebHunter MiniModule

import re


class Aws():
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'aws*', item[1], re.I) is not None
            w |= re.search(r'x-amz-id-[0-2]', item[0], re.I) is not None
            w |= re.search(r'x-amz-request-id', item[0], re.I) is not None
            if w:
                return 'Amazon Web Services Web Application Firewall (Amazon)'
                break
