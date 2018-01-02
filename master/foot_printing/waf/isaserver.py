#!/usr/bin/env python
# WebHunter MiniModule

import re


class Isaserver:
    @staticmethod
    def run(content):
        w = False
        w = re.search(
            r'The server denied the specified Uniform Resource Locator (URL). Contact the server administrator.',
            content,
            re.I) is not None
        w |= re.search(
            r'The ISA Server denied the specified Uniform Resource Locator (URL)',
            content,
            re.I) is not None
        if w:
            return "ISA Server (Microsoft)"
