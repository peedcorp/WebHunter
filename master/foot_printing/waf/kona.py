#!/usr/bin/env python
# WebHunter MiniModule

import re


class Kona:
    @staticmethod
    def run(content, code):
        w = False
        w = code == 501 and re.search(
            r"Reference #[0-9A-Fa-f.]+", content, re.I) is not None
        if w:
            return "KONA Security Solutions (Akamai Technologies)"
