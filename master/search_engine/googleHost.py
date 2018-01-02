#!/usr/bin/python
# WebHunter Run


class google_host:
    def __init__(self):
        pass

    def atom(self, host):
        import googleHostClass
        import re
        from core.urli import sansor
        from socket import gethostbyname

        host = sansor().pransor(host)

        if sansor().cransor(host):

            s = googleHostClass.googleHostClass(str(host).replace('.', '\.'))
            s.explore()
            hosts = s.hosts()
            return hosts
        else:
            return None

    def run(self):
        import sys

        W = '\x1b[37m'
        R = '\x1b[36m'
        C = '\x1b[32m'
        while True:
            host = raw_input('WH->[google host search] host: ')
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            wread = self.atom(host)
            if wread is None:
                print("\t[-] problem Connection (invalid URL or network) [-]")
                continue

            print('\n' + C)

            if wread == []:
                print("\tsubdomain not found.\n")
            else:
                for host in wread:
                    print('\t' + host)

            print('\n' + W)
            print('\t[Type exit to Exit]')
            print('\t[Type back to back]')
            break
