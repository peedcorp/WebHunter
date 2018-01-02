#!/usr/bin/env python
# WebHunter Run


class extract_links:
    def __init__(self):
        pass

    def atom(self, host):
        import urllib
        from core.urli import sansor
        import re

        host = sansor().pransor(host)
        if sansor().cransor(host):

            wread = urllib.urlopen('http://' + host).read()
            search = re.compile(host + r'/[\w\/\-.\?=%]+')
            content = search.findall(wread)
            if content == []:
                content.append('none')

            return content
        else:
            return None

    def run(self):
        from core.fsave import fsave
        import sys

        while True:
            host = raw_input('WH->[extract links] Host: ')
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            wread = self.atom(host)
            if wread is None:
                print("\t[-] problem Connection (invalid URL or network) [-]")
                continue

            wread = str(wread).replace(',', '<br>')
            saved = fsave(host, 'extract_links', wread).pansor()
            print(saved)
            print('\n\t[Type exit to Exit]')
            print('\t[Type back to Back]')
            break
