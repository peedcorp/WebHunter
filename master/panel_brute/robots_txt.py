#!/usr/bin/env python
# WebHunter Run


class robots_txt:
    def __init__(self):
        pass

    def atom(self, host):
        import request
        from urfil import sansor
        host = sansor().pransor(host)

        if sansor().cransor(host):
            payloads = [
                'robots.txt',
                'robot.xml',
                'robots.xml',
                'robot.txt',
                'robot.html']

            goods = []

            def getrequest(url):
                try:
                    getrequest = request.request(url)
                    if getrequest.status_code == 200:
                        if url not in goods:
                            goods.append(url)
                except BaseException:
                    pass

            for payload in payloads:
                getrequest(host + payload)
            if goods == []:
                goods.append('none')
            return goods
        else:
            return None

    def run(self):
        from core.fsave import fsave
        import sys

        while True:
            host = raw_input('WH->[robots txt] Host: ')
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            wread = self.atom(host)
            if wread is None:
                print("\t[-] problem Connection (invalid URL or network) [-]")
                continue
            if wread[0] == 'none':
                print("not found.")
                break

            wread = 'Activ url:' + str(wread).replace(',', '<br>')
            saved = fsave(host, 'robots_txt', wread).pansor()
            print(saved)
            print('\t[Type exit to Exit]')
            print('\t[Type back to Back]')
            break
