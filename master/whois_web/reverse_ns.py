#!/usr/bin/env python
# WebHunter Run


class reverse_ns:
    def __init__(self):
        pass

    def atom(self, host):
        import urllib
        from bs4 import BeautifulSoup
        from core.urli import sansor

        host = sansor().pransor(host)
        if sansor().cransor(host) and sansor().cransor('viewdns.info'):

            wread = urllib.urlopen(
                'http://www.viewdns.info/reversens/?ns=' + host).read()
            content = BeautifulSoup(
                wread, 'html.parser').find(
                'table', border='1')
            return content
        else:
            return None

    def run(self):
        import sys
        from core.fsave import fsave

        while True:
            host = raw_input('WH->[reverse ns] Host: ')
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            wread = self.atom(host)
            if wread is None:
                print("\t[-] problem Connection (invalid URL or network) [-]")
                continue

            saved = fsave(host, 'reverse_ns', wread).pansor()
            print(saved)
            print('\t[Type exit to Exit]')
            print('\t[Type back to back]')
            break
