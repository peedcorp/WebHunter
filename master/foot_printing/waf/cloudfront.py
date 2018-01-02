#!/usr/bin/env python
# WebHunter MiniModule

import re


class Cloudfront:
    @staticmethod
    def run(headers):
        w = False
        for item in headers.items():
            w = re.search(r'(cloudfront)', item[1], re.I) is not None
            w |= re.search('x-amz-cf-id', item[0], re.I) is not None
            if w:
                return "CloudFront Web Application Firewall (Amazon)"
                break
