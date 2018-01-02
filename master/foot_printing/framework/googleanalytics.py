#!/usr/bin/env python
# WebHunter MiniModule

import re


class Googleanalytics:
    @staticmethod
    def run(content):
        _ = False
        _ = re.search(
            r'GoogleAnalyticsObject|google-analytics\.com/analytics\.js',
            content,
            re.I) is not None
        _ |= re.search(r'Google Analytics Plugin', content, re.I) is not None
        if _:
            return "Google Analytics"
