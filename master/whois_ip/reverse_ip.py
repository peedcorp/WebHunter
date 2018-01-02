#!/usr/bin/env python
# WebHunter Run


class reverse_ip:
    def __init__(self):
        pass

    def atom(self, host):
        import urllib
        from core.urli import sansor

        host = sansor().pransor(host)
        if sansor().cransor(host) and sansor().cransor(
                'api.hackertarget.com/reverseiplookup'):

            wread = urllib.urlopen(
                'https://api.hackertarget.com/reverseiplookup/?q=' +
                host).read()
            return wread
        else:
            return None

    def run(self):
        from core.fsave import fsave
        import sys

        while True:
            host = raw_input('WH->[reverse ip] Host: ')
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            wread = self.atom(host)
            if wread is None:
                print("\t[-] problem Connection (invalid URL or network) [-]")
                continue

            saved = fsave(host, 'reverse_ip', wread).pansor()
            print(saved)
            print('\n\t[Type exit to Exit]')
            print('\t[Type back to Back]')
            break
