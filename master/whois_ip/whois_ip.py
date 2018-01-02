#!/usr/bin/env python
# WebHunter Run


class whois_ip:
    def __init__(self):
        pass

    def atom(self, host):
        import requests
        from core.urli import sansor
        from socket import gethostbyname

        host = sansor().pransor(host)
        if sansor().cransor(host) and sansor().cransor('ipapi.co'):

            url = gethostbyname(host)
            ipapi = 'https://ipapi.co/' + url + '/json'

            usage = {'user-agent': 'ipapi/ipapi-python/0.5.1'}

            rqs = requests.get(ipapi, headers=usage).json()
            return rqs
        else:
            return None

    def run(self):
        import sys

        W = '\x1b[37m'
        R = '\x1b[36m'
        C = '\x1b[32m'
        while True:
            host = raw_input('WH->[whois ip] Host: ')
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break
            index = [
                'ip',
                'city',
                'region',
                'country',
                'country_name',
                'postal',
                'latitude',
                'longitude',
                'timezone',
                'asn',
                'org']
            wread = self.atom(host)
            if wread is None:
                print("\t[-] problem Connection (invalid URL or network) [-]")
                continue

            for key in index:
                output = str(key) + ' : ' + str(wread[str(key)])
                print(C + '\t' + output + W)

            print('\t[Type exit to Exit]')
            print('\t[Type back to Back]')
            break
