#!/usr/bin/python
# WebHunter Run


class all_mail:
    def __init__(self):
        pass

    def atom(self, host):

        import bingMailClass
        import googleMailClass
        import yahooMailClass
        from core.urli import sansor

        sans = sansor()
        host = sans.pransor(host)

        if sans.cransor(host):

            this = []
            a = bingMailClass.bingMailClass(host)
            a.explore()
            emails1 = a.emails()

            b = googleMailClass.googleMailClass(host)
            b.explore()
            emails2 = b.emails()

            c = yahooMailClass.yahooMailClass(host)
            c.explore()
            emails3 = c.emails()

            for em1 in emails1:
                if em1 not in this:
                    this.append(em1)
                for em2 in emails2:
                    if em2 not in this:
                        this.append(em2)
                    for em3 in emails3:
                        if em3 not in this:
                            this.append(em3)

            return this
        else:
            return None

    def run(self):
        import sys

        W = '\x1b[37m'
        R = '\x1b[36m'
        C = '\x1b[32m'
        while True:
            host = raw_input('WH->[all engine email search] Host: ')
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            wread = self.atom(host)
            if wread is None:
                print("\t[-] problem Connection (invalid URL or network) [-]")
                continue

            if wread == []:
                print("\temail not found.\n")
                break

            print('\n' + C)
            for email in wread:
                print('\t' + email)

            print('\n' + W)
            print('\t[Type exit to Exit]')
            print('\t[Type back to back]')
            break
