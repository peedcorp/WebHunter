#!/usr/bin/env python
# WebHunter MiniModule

import re


class Bolt:
    @staticmethod
    def run(content):
        _ = False
        try:
            _ = re.search(r'bolt|styles/bolt.css', content) is not None
            _ |= re.search(
                r'/favicon-bolt.ico|theme/bolt-v300|bolt-slideshow|bolt3-slide-responsive.png',
                content) is not None
            if _:
                return "Bolt"
        except Exception as e:
            pass
