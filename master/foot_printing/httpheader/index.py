#!/usr/bin/env python
# WebHunter Run


class httpheader:
    def __init__(self):
        pass

    def atom(self, host):
        import urllib
        import header
        from core.urli import sansor
        host = sansor().pransor(host)
        if sansor().cransor(host):
            content = urllib.urlopen('http://' + host).headers
            header = header.Headers.run(content)
            return header
        else:
            return None

    def run(self):
        import sys
        from core.fsave import fsave

        while True:
            host = raw_input('WH->[http header] Host: ')
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            wread = self.atom(host)

            if wread is None:
                print("\t[-] problem Connection (invalid URL or network) [-]")
                continue

            saved = fsave(host, 'http_header', wread).pansor()
            print(saved)
            print('\t[Type exit to Exit]')
            print('\t[Type back to Back]')
            break
