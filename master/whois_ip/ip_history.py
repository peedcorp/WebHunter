#!/usr/bin/env python
# WebHunter Run


class ip_history:
    def __init__(self):
        pass

    def atom(self, host):
        import urllib
        from bs4 import BeautifulSoup
        from core.urli import sansor

        host = sansor().pransor(host)
        if sansor().cransor(host) and sansor().cransor('viewdns.info'):

            wread = urllib.urlopen(
                'http://www.viewdns.info/iphistory/?domain=' + host).read()
            content = BeautifulSoup(
                wread, 'html.parser').find(
                'font', face='Courier')
            content = str(content).replace('''<script class="stripe-button" data-amount="19900" data-currency="usd" data-description="Full report for 'google.com'" data-image="/images/ok.GIF" data-key="pk_live_ey9TT0KvaFQoLWRyDYg9oqQd" data-label="Download The Full Report for $199" data-name="" src="https://checkout.stripe.com/checkout.js"></script>''', '')
            return content
        else:
            return None

    def run(self):
        from core.fsave import fsave
        import sys

        while True:
            host = raw_input('WH->[ip history] Host: ')
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            content = self.atom(host)
            if content is None:
                print("\t[-] problem Connection (invalid URL or network) [-]")
                continue

            saved = fsave(host, 'ip_history', content).pansor()
            print(saved)
            print('\n\t[Type exit to Exit]')
            print('\t[Type back to Back]')
            break
