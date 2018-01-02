#!/usr/bin/env python
# WebHunter MiniModule

import re


class Secureiis:
    @staticmethod
    def run(content):
        w = False
        w = re.search(
            r'SecureIIS[^<]+Web Server Protection',
            content,
            re.I) is not None
        w |= re.search(
            r'http://www.eeye.com/SecureIIS/',
            content,
            re.I) is not None
        w |= re.search(
            r'\?subject=[^>]*SecureIIS Error',
            content,
            re.I) is not None
        if w:
            return "SecureIIS Web Server Security (BeyondTrust"
