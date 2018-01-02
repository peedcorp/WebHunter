#!/usr/bin/env python
# WebHunter MiniModule

import re


class Concrete5:
    @staticmethod
    def run(content):
        _ = False
        try:
            _ = re.search(
                r'concrete5_theme|content="concrete5',
                content) is not None
            _ |= re.search(r'/themes/concrete5', content) is not None
            if _:
                return "concrete5"
        except Exception as e:
            pass
