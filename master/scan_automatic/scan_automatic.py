#!/usr/bin/env python
# WebHunter Run


class scan_automatic:
    def __init__(self):
        pass

    def clean(self, string):
        chars = ['"', "'", 'u"', "u'", '[', ']', '["',
                 ']"', '[u"', "[u'", '{u"', "{u'", '\t', '\n']
        for char in chars:
            string = str(string).replace(char, '')
        return string.replace(',', '<br>')

    def atom(self, host):
        import master
        from core.urli import sansor

        host = sansor().pransor(host)
        if sansor().cransor(host):
            cloudflare = master.dns_explore.cloud_flare().atom(host)
            extractlinks = master.dns_explore.extract_links().atom(host)
            whoisip = master.whois_ip.whois_ip().atom(host)
            cms = master.foot_printing.cms.cms().atom(host)
            os = master.foot_printing.os.os().atom(host)
            framework = master.foot_printing.framework.framework().atom(host)
            language = master.foot_printing.language.language().atom(host)
            waf = master.foot_printing.waf.waf().atom(host)
            httpheader = master.foot_printing.httpheader.httpheader().atom(host)
            allmail = master.search_engine.all_mail().atom(host)
            allhost = master.search_engine.all_host().atom(host)
            robotstxt = master.panel_brute.robots_txt().atom(host)
            cloudflare = 'cloudflare or dns : {' + self.clean(
                cloudflare) + ' } <br><br>'
            extractlinks = 'all links page : {' + self.clean(
                extractlinks) + ' } <br><br>'
            whoisip = 'information ip : {' + \
                self.clean(whoisip) + ' } <br><br>'
            allmail = 'all emails : {' + self.clean(allmail) + ' } <br><br>'
            allhost = 'all subdomain : {' + self.clean(allhost) + ' } <br><br>'
            robotstxt = 'robots.txt : {' + \
                self.clean(robotstxt) + ' } <br><br>'
            cms = 'foot printing : {<br>cms this web is ' + self.clean(
                cms) + '<br>'
            os = 'os this web is ' + self.clean(os) + '<br> '
            language = 'language this web is ' + \
                self.clean(language) + '<br>framework : '
            framework = self.clean(framework) + '<br>waf : '
            waf = self.clean(waf) + '<br>'
            httpheader = self.clean(httpheader) + ' }<br><br>'

            result = {'cloud_flare': cloudflare, 'extract_links': extractlinks,
                      'whois_ip': whoisip, 'cms': cms,
                      'os': os, 'framework': framework, 'language': language,
                      'waf': waf, 'httpheader': httpheader, 'allmail': allmail,
                      'allhost': allhost, 'robots_txt': robotstxt
                      }
            return result
        else:
            return None

    def run(self):
        from core.fsave import fsave
        import sys

        while True:
            host = raw_input('WH->[scan automatic] Host: ')
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            wread = self.atom(host)
            if wread is None:
                print("\t[-] problem Connection (invalid URL or network) [-]")
                continue

            final = [
                wread['cloud_flare'],
                wread['extract_links'],
                wread['whois_ip'],
                wread['allmail'],
                wread['allhost'],
                wread['robots_txt'],
                wread['cms'],
                wread['os'],
                wread['language'],
                wread['framework'],
                wread['waf'],
                wread['httpheader']]

            final = self.clean(final)
            saved = fsave(host, 'scan_automatic', str(final)).pansor()
            print(saved)
            print('\n\t[Type exit to Exit]')
            print('\t[Type back to Back]')
            break
