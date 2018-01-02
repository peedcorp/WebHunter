#!/usr/bin/env python
# WebHunter MiniModule

import re


class Sonicwall:
    @staticmethod
    def run(content):
        w = False
        w = re.search(
            r'This request is blocked by the SonicWALL',
            content,
            re.I) is not None
        w |= re.search(
            r'Web Site Blocked.+\bnsa_banner',
            content,
            re.I) is not None
        if w:
            return "SonicWALL (Dell)"
