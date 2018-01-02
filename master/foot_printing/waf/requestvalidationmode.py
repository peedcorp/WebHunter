#!/usr/bin/env python
# WebHunter MiniModule

import re


class Requestvalidationmode:
    @staticmethod
    def run(content):
        w = False
        w = re.search(
            r'ASP.NET has detected data in the request that is potentially dangerous',
            content,
            re.I) is not None
        w |= re.search(
            r'Request Validation has detected a potentially dangerous client input value',
            content,
            re.I) is not None
        if w:
            return "ASP.NET RequestValidationMode (Microsoft)"
