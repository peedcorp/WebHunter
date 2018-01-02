#!/usr/bin/env python
# WebHunter Run


class domain_map:
    def __init__(self):
        pass

    def atom(self, host, fname):
        import urllib
        from core.urli import sansor

        host = sansor().pransor(host)
        if sansor().cransor(host) and sansor().cransor('dnsdumpster.com'):
            try:
                content = urllib.urlretrieve(
                    'https://dnsdumpster.com/static/map/' + host + '.png',
                    fname)
                return True
            except BaseException:
                return "\tUnfortunately, the file could not be saved"

        else:
            return None

    def run(self):
        from random import randint
        import sys

        while True:
            host = raw_input('WH->[domain_map] Host: ')
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            rand = str(randint(0, 2000))
            fname = 'output/' + rand + '_domain_map.png'
            wread = self.atom(host, fname)

            if wread:
                print('\tresult saved in ' + fname)
            elif wread is None:
                print("\t[-] problem Connection (invalid URL or network) [-]")
                continue
            else:
                print wread
                break

            print('\n\t[Type exit to Exit]')
            print('\t[Type back to Back]')
            break
