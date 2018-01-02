#!/usr/bin/python
# WebHounter Run


class google_mail:
    def __init__(self):
        pass

    def atom(self, host):
        import googleMailClass
        from core.urli import sansor

        host = sansor().pransor(host)

        if sansor().cransor(host):
            s = googleMailClass.googleMailClass(host)
            s.explore()
            emails = s.emails()
            return emails
        else:
            return None

    def run(self):
        import sys

        W = '\x1b[37m'
        R = '\x1b[36m'
        C = '\x1b[32m'
        while True:
            host = raw_input('WH->[google email search] Host: ')
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
                print("\temail not found.\n")
            else:
                for email in wread:
                    print('\t' + email)
            print('\n' + W)
            print('\t[Type exit to Exit]')
            print('\t[Type back to back]')
            break
