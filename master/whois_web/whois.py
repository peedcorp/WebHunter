#!/usr/bin/env python
# WebHunter Run


class whois:
    def __init__(self):
        pass

    def atom(self, host):
        import urllib
        from bs4 import BeautifulSoup
        from core.urli import sansor

        host = sansor().pransor(host)
        if sansor().cransor(host) and sansor().cransor('viewdns.info'):

            wread = urllib.urlopen(
                'http://www.viewdns.info/whois/?domain=' + host).read()
            content = BeautifulSoup(
                wread, 'html.parser').find(
                'font', face='Courier')
            return content
        else:
            return None

    def run(self):
        from core.fsave import fsave
        import sys

        while True:
            host = raw_input('WH->[whois] Host: ')
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            wread = self.atom(host)
            if wread is None:
                print("\t[-] problem Connection (invalid URL or network) [-]")
                continue

            saved = fsave(host, 'whois', wread).pansor()
            print(saved)
            print('\n\t[Type exit to Exit]')
            print('\t[Type back to Back]')
            break
