#!/usr/bin/env python
# WebHunter Run


class framework:
    def __init__(self):
        pass

    def atom(self, host):
        import cakephp
        import cherrypy
        import django
        import flask
        import fuelphp
        import grails
        import larvel
        import mvc
        import nette
        import phalcon
        import rails
        import symfony
        import yii
        import zend
        import googleanalytics
        import jquery
        import urllib
        from core.urli import sansor

        host = sansor().fransor(host)
        hostp = sansor().pransor(host)
        if sansor().cransor(hostp):

            header = urllib.urlopen(host).headers
            cont = urllib.urlopen(host).read()
            final = []
            ckp = cakephp.Cakephp().run(header)
            cpy = cherrypy.Cherrypy().run(header)
            djo = django.Django().run(header)
            fls = flask.Flask().run(header)
            flp = fuelphp.Fuelphp().run(header, cont)
            grl = grails.Grails().run(header)
            lrv = larvel.Larvel().run(header)
            mvc = mvc.Mvc().run(header)
            nte = nette.Nette().run(header)
            pcn = phalcon.Phalcon().run(header)
            rls = rails.Rails().run(header)
            sfy = symfony.Symfony().run(header)
            yii = yii.Yii().run(header, cont)
            znd = zend.Zend().run(header)
            gas = googleanalytics.Googleanalytics().run(cont)
            jqr = jquery.Jquery().run(cont)

            eve = [
                ckp, cpy, djo,
                fls, flp, grl,
                lrv, mvc, nte,
                pcn, rls, sfy,
                yii, znd, gas,
                jqr]

            for key in eve:
                if key:
                    final.append(key)
            if final == []:
                final.append('none')
            return final
        else:
            return None

    def run(self):
        import sys

        W = '\x1b[37m'
        R = '\x1b[36m'
        C = '\x1b[32m'
        while True:
            host = raw_input('WH->[framework Footprinting] Host: ')
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
                        '\n\tThe [{name}] framework is active on the server ' +
                        W).format(
                        name=key)
                else:
                    coun = coun + 1

            if coun == 16:
                print('\tNo framework found.')

            print('\n\t[Type exit to Exit]')
            print('\t[Type back to Back]')
            break
