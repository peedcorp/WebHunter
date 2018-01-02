#!/usr/bin/env python
# WebHunter Run


class os:
    def __init__(self):
        pass

    def atom(self, host):
        import bsd
        import linux
        import mac
        import solaris
        import unix
        import windows
        import urllib
        from core.urli import sansor
        host = sansor().fransor(host)
        hostp = sansor().pransor(host)
        if sansor().cransor(hostp):
            header = urllib.urlopen(host).headers
            final = []
            bsd = bsd.Bsd().run(header)
            lnx = linux.Linux().run(header)
            mac = mac.Mac().run(header)
            slr = solaris.Solaris().run(header)
            unx = unix.Unix().run(header)
            win = windows.Windows().run(header)

            eve = [bsd, lnx, mac, slr, unx, win]
            for key in eve:
                if key:
                    final.append(key)
            if final == []:
                final.append('none')
            return final
        else:
            return None

    def run(self):
        import sys

        W = '\x1b[37m'
        R = '\x1b[36m'
        C = '\x1b[32m'
        while True:
            host = raw_input('WH->[os Footprinting] Host: ')
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            wread = self.atom(host)
            if wread is None:
                print("\t[-] problem Connection (invalid URL or network) [-]")

            coun = 0
            for key in wread:
                if key:
                    print(C + '\n\tos this web is ' + key + W)
                    break
                coun = coun + 1
            if coun == 6:
                print('\n\tos not identify.')

            print('\n\t[Type exit to Exit]')
            print('\t[Type back to Back]')
            break
