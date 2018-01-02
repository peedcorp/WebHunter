#!/usr/bin/python
# WebHunter MiniModule


class yahooMailClass:

    def __init__(self, host):
        self.host = host
        self.nextresults = ''
        self.core = 'search.yahoo.com'
        self.userAgent = '(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6'
        self.limit = 100
        self.count = 0

    def searcher(self):
        import httplib
        h = httplib.HTTP(self.core)
        h.putrequest('GET', '/search?p=\'%40' + self.host + '\'&b=' +
                     str(self.count) + '&pz=10')
        h.putheader('Host', self.core)
        h.putheader('User-agent', self.userAgent)
        h.endheaders()
        returncode, returnmsg, headers = h.getreply()

        self.nextresults += h.getfile().read()

    def emails(self):
        import soup
        rawres = soup.parser(self.nextresults, self.host)
        return rawres.emails()

    def explore(self):
        while self.count <= self.limit and self.count <= 1000:
            self.searcher()
            self.count += 10
