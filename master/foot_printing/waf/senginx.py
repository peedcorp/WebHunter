#!/usr/bin/env python
# WebHunter MiniModule

import re


class Senginx:
    @staticmethod
    def run(content):
        w = False
        w = re.search(r"SENGINX-ROBOT-MITIGATION", content, re.I) is not None
        if w:
            return "SEnginx (Neusoft Corporation)"
