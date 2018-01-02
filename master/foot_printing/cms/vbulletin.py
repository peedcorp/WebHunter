#!/usr/bin/env python
# WebHunter MiniModule

import re


class Vbulletin:
    @staticmethod
    def run(content):
        _ = False
        try:
            _ = re.search(r'/vbulletin/default', content) is not None
            _ |= re.search(r'"/vb_home_logo1.png', content) is not None
            if _:
                return "Vbulletin"
        except Exception as e:
            pass
