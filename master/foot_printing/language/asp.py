#!/usr/bin/env python
# WebHunter MiniModule

import re


class Asp:
    @staticmethod
    def run(content, headers):
        _ = False
        for item in headers.items():
            _ = re.search(
                r'ASP.NET|X-AspNet-Version|x-aspnetmvc-version',
                str(item),
                re.I) is not None
            if not _:
                _ |= re.search(r'(__VIEWSTATE\W*)', content) is not None
            if not _:
                _ |= re.search(r'\.asp$|\.aspx$', content) is not None
            if _:
                return "ASP.NET"
                break
