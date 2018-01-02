#!/usr/bin/env python
# WebHunter MiniModule

import re


class Mvc:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(
                r'x-aspnetmvc-version|__requestverificationtoken',
                str(item),
                re.I) is not None
            if _:
                return "ASP.NET MVC"
                break
