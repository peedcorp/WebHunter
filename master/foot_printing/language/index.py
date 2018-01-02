#!/usr/bin/env python
# WebHunter Run


class language:
    def __init__(self):
        pass

    def atom(self, host):
        import asp
        import java
        import php
        import python
        import ruby
        import perl
        import urllib
        from core.urli import sansor

        host = sansor().fransor(host)
        hostp = sansor().pransor(host)
        if sansor().cransor(hostp):

            content = urllib.urlopen(host).read()
            header = urllib.urlopen(host).headers
            final = []
            asp = asp.Asp().run(content, header)
            jva = java.Java().run(content, header)
            php = php.Php().run(content, header)
            prl = perl.Perl().run(content, header)
            pyt = python.Python().run(content, header)
            rby = ruby.Ruby().run(content, header)

            eve = [asp, jva, php, prl, pyt, rby]
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
            host = raw_input('WH->[language Footprinting] Host: ')
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            wread = self.atom(host)
            if wread is None:
                print("\t[-] problem Connection (invalid URL or network) [-]")
                continue

            coun = 0
            for key in wread:
                if key:
                    print(C + '\n\tlanguage this web is ' + key + W)
                    break
                coun = coun + 1
            if coun == 6:
                print('\n\tlanguage not identify.')

            print('\n\t[Type exit to Exit]')
            print('\t[Type back to Back]')
            break
