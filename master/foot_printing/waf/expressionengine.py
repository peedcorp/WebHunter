#!/usr/bin/env python
# WebHunter MiniModule

import re


class Expressionengine:
    @staticmethod
    def run(content):
        w = False
        w = re.search(r"Invalid GET Data", content, re.I) is not None
        if w:
            return "ExpressionEngine (EllisLab)"
