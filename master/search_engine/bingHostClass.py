#!/usr/bin/python
# WebHunter MiniModule


class bingHostClass:

    def __init__(self, host):
        self.host = host
        self.results = ''
        self.nextresults = ''
        self.core = 'www.bing.com'
        self.userAgent = '(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6'
        self.quantity = '50'
        self.limit = 100
        self.count = 10

    def searcher(self):
        import httplib
        h = httplib.HTTP(self.core)
        h.putrequest(
            'GET', '/search?q=' + self.host + '&count=50&first=' +
            str(self.count))
        h.putheader('Host', self.core)
        h.putheader(
            'Cookie',
            'mkt=en-US;ui=en-US;SRCHHPGUSR=NEWWND=0&ADLT=DEMOTE&NRSLT=50')
        h.putheader('Accept-Language', 'en-us,en')
        h.putheader('User-agent', self.userAgent)
        h.endheaders()
        returncode, returnmsg, headers = h.getreply()
        self.results = h.getfile().read()
        self.nextresults += self.results

    def hosts(self):
        import soup
        rawres = soup.parser(self.nextresults, self.host)
        return rawres.hostnames_all()

    def explore(self):
        while (self.count < self.limit):
            self.searcher()
            self.count += 50
