#!/usr/bin/env python
# WebHunter Run


class waf:
    def __init__(self):
        pass

    def atom(self, host):
        import airlock
        import anquanboa
        import aws
        import baidu
        import barracuda
        import bigip
        import binarysec
        import blockdos
        import chinacache
        import ciscoacexml
        import cloudflare
        import cloudfront
        import denyall
        import dotdefender
        import expressionengine
        import edgecast
        import fortiweb
        import hyperguard
        import incapsula
        import isaserver
        import jiasule
        import knownsec
        import kona
        import modsecurity
        import netcontinuum
        import paloalto
        import profense
        import radware
        import requestvalidationmode
        import safedog
        import secureiis
        import senginx
        import sitelock
        import sonicwall
        import sucuri
        import teros
        import trafficshield
        import urlscan
        import uspses
        import varnish
        import wallarm
        import webknight
        import urllib
        from core.urli import sansor
        host = sansor().fransor(host)
        hostp = sansor().pransor(host)
        if sansor().cransor(hostp):
            target = urllib.urlopen(host)
            header = target.headers
            cont = target.read()
            code = target.code
            final = []
            air = airlock.Airlock().run(header)
            anq = anquanboa.Anquanboa().run(header)
            aws = aws.Aws().run(header)
            bid = baidu.Baidu().run(header)
            brc = barracuda.Barracuda().run(header)
            bgp = bigip.Bigip().run(header)
            brs = binarysec.Binarysec().run(header)
            bkd = blockdos.Blockdos().run(header)
            chi = chinacache.Chinacache().run(header)
            cix = ciscoacexml.Ciscoacexml().run(header)
            cdl = cloudflare.Cloudflare().run(header)
            cdr = cloudfront.Cloudfront().run(header)
            dna = denyall.Denyall().run(cont, code, header)
            dfn = dotdefender.Dotdefender().run(header)
            exp = expressionengine.Expressionengine().run(cont)
            edg = edgecast.Edgecast().run(header)
            fwb = fortiweb.Fortiweb().run(header)
            hpg = hyperguard.Hyperguard().run(header)
            ics = incapsula.Incapsula().run(header)
            isv = isaserver.Isaserver().run(cont)
            jsl = jiasule.Jiasule().run(cont, header)
            kns = knownsec.Knownsec().run(cont)
            kna = kona.Kona().run(cont, code)
            msc = modsecurity.Modsecurity().run(header)
            ncm = netcontinuum.Netcontinuum().run(header)
            pto = paloalto.Paloalto().run(header)
            pfs = profense.Profense().run(header)
            rdw = radware.Radware().run(header)
            rvm = requestvalidationmode.Requestvalidationmode().run(cont)
            sfd = safedog.Safedog().run(header)
            sci = secureiis.Secureiis().run(cont)
            snx = senginx.Senginx().run(cont)
            slk = sitelock.Sitelock().run(cont)
            swl = sonicwall.Sonicwall().run(cont)
            scr = sucuri.Sucuri().run(header)
            trs = teros.Teros().run(header)
            tfs = trafficshield.Trafficshield().run(header)
            usc = urlscan.Urlscan().run(header)
            usp = uspses.Uspses().run(header)
            vns = varnish.Varnish().run(header)
            wlm = wallarm.Wallarm().run(header)
            wkt = webknight.Webknight().run(header)

            eve = [
                air, anq, aws,
                bid, brc, bgp,
                brs, bkd, chi,
                cix, cdl, cdr,
                dfn, dna, exp,
                edg, fwb, hpg,
                ics, isv, jsl,
                kns, kna, msc,
                ncm, pto, pfs,
                rdw, rvm, sfd,
                sci, snx, slk,
                swl, scr, trs,
                tfs, usc, usp,
                vns, wlm, wkt]

            for key in eve:
                if key:
                    final.append(key)
            if final == []:
                final.append('none')
            return final

        else:
            return None

    def run(self):
        from core.fsave import fsave
        import sys

        W = '\x1b[37m'
        R = '\x1b[36m'
        C = '\x1b[32m'
        while True:
            host = raw_input('WH->[waf Footprinting] Host: ')
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
                    print(
                        C +
                        '\n\tThe {name}-security program is active on the server ' +
                        W).format(
                        name=key)
                else:
                    coun = coun + 1

            if coun == 42:
                print('\tNo security apps detected.')

            print('\n\t[Type exit to Exit]')
            print('\t[Type back to Back]')
            break
