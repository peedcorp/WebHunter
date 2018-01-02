#!/usr/bin/env python
# WebHunter MiniModule

import re


class Typo3:
    @staticmethod
    def run(content):
        _ = False
        try:
            _ = re.search(
                r'This website is powered by TYPO3|/typo3conf',
                content) is not None
            _ |= re.search(
                r'"generator" content="TYPO3 CMS">|/typo3temp/assets/',
                content) is not None
            if _:
                return "Typo3"
        except Exception as e:
            pass
