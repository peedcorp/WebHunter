#!/usr/bin/env python
# WebHunter Run


class web_robot:
    def __init__(self):
        pass

    def atom(self, host, tag):
        from urllib import urlopen, unquote
        from bs4 import BeautifulSoup
        from core.urli import sansor

        def _reading(html, tag):
            soup = BeautifulSoup(html, 'html.parser').find_all(tag)
            if soup == []:
                soup.append('none')
            else:
                return soup

        def _script(html):
            soup = BeautifulSoup(
                html, 'html.parser').find_all(
                'script', src=True)

            if soup == []:
                soup.append('none')
            else:
                script = []
                for link in soup:
                    link = link.get('src')
                    script.append(unquote(link))
                return script

        def _link(html):
            soup = BeautifulSoup(
                html, 'html.parser').find_all(
                'link', href=True)

            if soup == []:
                soup.append('none')
            else:
                link = []
                for key in soup:
                    key = key.get('href')
                    link.append(unquote(key))
                return link

        def _img(html):
            soup = BeautifulSoup(html, 'html.parser').find_all('img', src=True)

            if soup == []:
                soup.append('none')
            else:
                img = []
                for key in soup:
                    key = key.get('src')
                    img.append(unquote(key))
                return img

        host = sansor().pransor(host)
        if sansor().cransor(host):
            html = urlopen('http://' + host).read()
            if tag == 'img':
                wread = _img(html)
            elif tag == 'link':
                wread = _link(html)
            elif tag == 'script':
                wread = _script(html)
            else:
                wread = _reading(html, tag)

            return wread
        else:
            return None

    def run(self):
        from core.fsave import fsave
        import sys

        while True:
            host = raw_input('WH->[web robot] Host: ')

            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            option = '''\n1> a\n2> meta tag\n3> input \n4> form\n5> iframe\n6> h1\n7>script\n8> img\n9> all photo link\n10> all script page link\n11>all css page link\n'''

            while True:
                print(option)
                what = raw_input('WH->[robot] select option: ')
                if host == 'exit':
                    sys.exit()
                elif host == 'back':
                    break
                elif what == '1':
                    recv = self.atom(host, 'a')
                elif what == '2':
                    recv = self.atom(host, 'meta')
                elif what == '3':
                    recv = self.atom(host, 'input')
                elif what == '4':
                    recv = self.atom(host, 'form')
                elif what == '5':
                    recv = self.atom(host, 'iframe')
                elif what == '6':
                    recv = self.atom(host, 'h1')
                elif what == '7':
                    recv = self.atom(host, 'script')
                elif what == '8':
                    recv = self.atom(host, 'img')
                elif what == '9':
                    recv = self.atom(host, 'img')
                elif what == '10':
                    recv = self.atom(host, 'script')
                elif what == '11':
                    recv = self.atom(host, 'link')
                elif what == 'exit':
                    sys.exit()
                elif what == '':
                    continue
                else:
                    continue
                break

            if recv is None:
                print("\t[-] problem Connection (invalid URL or network) [-]")
                continue

            length = "all : " + str(len(recv)) + "<br>"
            wread = str(recv).replace('<', '')
            wread = wread.replace(',', '<br>')
            wread = fsave(host, 'web_robot', length + wread).pansor()
            print(wread)
            print('\t[Type exit to Exit]')
            print('\t[Type back to Back]')
            break
