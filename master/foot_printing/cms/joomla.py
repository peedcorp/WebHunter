#!/usr/bin/env python
# WebHunter MiniModule

import re


class Joomla:
    @staticmethod
    def run(content):
        _ = False
        try:
            _ = re.search(
                r'/index.php?option=(\S*)|<meta name="generator" content="Joomla*|Powered by <a href="http://www.joomla.org">Joomla!</a>*',
                content) is not None
            if _:
                if re.search('/templates/*', content, re.I):
                    return "Joomla"
        except Exception as e:
            pass
