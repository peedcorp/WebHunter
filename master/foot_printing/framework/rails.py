#!/usr/bin/env python
# WebHunter MiniModule

import re


class Rails:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(
                r'rails*|_rails_admin_session=*|x-rails',
                item[1],
                re.I) is not None
            _ |= re.search(r'rails*|x-rails', item[0], re.I) is not None
            if _:
                return "Rails (Ruby)"
                break
