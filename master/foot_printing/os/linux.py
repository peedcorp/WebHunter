#!/usr/bin/env python
# WebHunter MiniModule

import re


class Linux:
    @staticmethod
    def run(os):
        for item in os.items():
            _ = re.findall(
                r'linux|ubuntu|gentoo|debian|dotdeb|centos|redhat|sarge|etch|lenny|squeeze|wheezy|jessie|red hat|scientific linux',
                str(item),
                re.I)
            if _:
                if len(_) == 2:
                    return _[0]
                else:
                    return _[0]
                break
