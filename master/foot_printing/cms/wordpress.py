#!/usr/bin/env python
# WebHunter MiniModule

import re


class Wordpress:
    @staticmethod
    def run(content):
        _ = False
        try:
            for x in ('/wp-admin/', '/wp-content/', '/wp-includes/',
                      '<meta name="generator" content="WordPress'):
                _ = re.search(x, content) is not None
                if _:
                    return "Wordpress"
                    break
        except Exception as e:
            pass
