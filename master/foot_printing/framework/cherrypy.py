#!/usr/bin/env python
# WebHunter MiniModule

import re


class Cherrypy:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'CherryPy', item[1], re.I) is not None
            if _:
                return "CherryPy (Python)"
                break
