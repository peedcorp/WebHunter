#!/usr/bin/env python
# WebHunter Run


class cms:
    def __init__(self):
        pass

    def atom(self, host):
        import drupal
        import joomla
        import wordpress
        import magento
        import concrete5
        import bolt
        import typo3
        import vbulletin
        import urllib
        from core.urli import sansor
        host = sansor().fransor(host)
        hostp = sansor().pransor(host)
        if sansor().cransor(hostp):

            cont = urllib.urlopen(host).read()
            final = []
            drp = drupal.Drupal().run(cont)
            jml = joomla.Joomla().run(cont)
            wps = wordpress.Wordpress().run(cont)
            mgt = magento.Magento().run(cont)
            cr5 = concrete5.Concrete5().run(cont)
            blt = bolt.Bolt().run(cont)
            tp3 = typo3.Typo3().run(cont)
            vbn = vbulletin.Vbulletin().run(cont)
            eve = [drp, jml, wps, mgt, cr5, blt, tp3, vbn]
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
            host = raw_input('WH->[cms Footprinting] Host: ')
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
                    print(C + '\n\tcms this web is ' + key + W)
                    break
                coun = coun + 1
            if coun == 8:
                print('\n\tcms not identify.')

            print('\n\t[Type exit to Exit]')
            print('\t[Type back to Back]')
            break
