#!/usr/bin/env python
# WebHunter MiniModule

import re


class Blockdos:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'BlockDos[\.net]*', item[1], re.I) is not None
            if w:
                return "BlockDoS"
                break
