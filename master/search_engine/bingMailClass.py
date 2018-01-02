#!/usr/bin/python
# WebHunter MiniModule



class bingMailClass:

    def __init__(self, host):
        self.host = host.replace(' ', '%20')
        self.results = ''
        self.nextresults = ''
        self.core = 'www.bing.com'
        self.userAgent = '(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6'
        self.limit = 100
        self.count = 10

    def searcher(self):
        import httplib
        h = httplib.HTTP(self.core)
        h.putrequest(
            'GET', '/search?q=%40' + self.host + '&count=50&first=' +
            str(self.count))
        h.putheader('Host', self.core)
        h.putheader('Cookie', 'SRCHHPGUSR=ADLT=DEMOTE&NRSLT=50')
        h.putheader('Accept-Language', 'en-us,en')
        h.putheader('User-agent', self.userAgent)
        h.endheaders()
        returncode, returnmsg, headers = h.getreply()
        self.results = h.getfile().read()
        self.nextresults += self.results

    def emails(self):
        import soup
        rawres = soup.parser(self.nextresults, self.host)
        return rawres.emails()

    def explore(self):
        while (self.count < self.limit):
            self.searcher()
            self.count += 50
