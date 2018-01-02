#!/usr/bin/python
# WebHunter MiniModule


class googleMailClass:

    def __init__(self, host):
        self.host = host
        self.results = ""
        self.nextresults = ""
        self.core = "www.google.com"
        self.userAgent = "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"
        self.quantity = "100"
        self.limit = 100
        self.count = 10

    def searcher(self):
        import requests
        urly = "http://" + self.core + "/search?num=" + self.quantity + \
            "&start=" + str(self.count) + "&hl=en&meta=&q=%40\"" + self.host + "\""
        r = requests.get(urly)
        self.results = r.content
        self.nextresults += self.results

    def emails(self):
        import soup
        rawres = soup.parser(self.nextresults, self.host)
        return rawres.emails()

    def explore(self):
        while self.count <= self.limit and self.count <= 1000:
            self.searcher()
            self.count += 100
