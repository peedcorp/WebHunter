#!/usr/bin/env python
# WebHunter MiniModule

import re


class Php():
    @staticmethod
    def run(content, headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'X-PHP-PID|PHP\S*|PHPSESSID', str(item)) is not None
            _ |= re.search(r'.php|.phtml', content) is not None
            if _:
                return "PHP"
                break
