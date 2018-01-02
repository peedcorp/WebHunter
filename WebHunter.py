#!/usr/bin/python
import signal
import sys
import platform
import master


W = "\x1b[37m"
R = "\x1b[36m"

if platform.system() not in ["Linux", "Darwin"]:
    print("[!] Sorry, this tool is designed for Linux and Mac !")
    sys.exit()


def c(signal, s):
    pass


signal.signal(signal.SIGINT, c)


def start():

    def banner():
        print('''
        db   d8b   db d88888b d8888b.
        88   I8I   88 88'     88  `8D
        88   I8I   88 88ooooo 88oooY'
        Y8   I8I   88 88~~~~~ 88~~~b.
        `8b d8'8b d8' 88.     88   8D
         `8b8' `8d8'  Y88888P Y8888P'


        db   db db    db d8b   db d888888b d88888b d8888b.
        88   88 88    88 888o  88 `~~88~~' 88'     88  `8D
        88ooo88 88    88 88V8o 88    88    88ooooo 88oobY'
        88~~~88 88    88 88 V8o88    88    88~~~~~ 88`8b
        88   88 88b  d88 88  V888    88    88.     88 `88.
        YP   YP ~Y8888P' VP   V8P    YP    Y88888P 88   YD

        ''')

    def guide():
        print("-----------------------------------------")
        print("1> dns anaysis && explore && web Scraping|")
        print("-----------------------------------------|")
        print("2> finger ip                             |")
        print("-----------------------------------------|")
        print("3> panel brute                           |")
        print("-----------------------------------------|")
        print("4> who's                                 |")
        print("-----------------------------------------|")
        print("5> foot printing                         |")
        print("-----------------------------------------|")
        print("6> Search Engine                         |")
        print("-----------------------------------------|")
        print("7> scan automatic                        |")
        print("-----------------------------------------|")
        print("Exit> exit                               |")
        print("-----------------------------------------\n")

    def dns_explore():
        def guide():
            print("\n1> dnslookup => View all DNS records for specified domain.")
            print(
                "2> domain map => Viewing all DNS records for your domain is displayed in the image format.")
            print("3> dns report => Provides a complete report on your DNS settings.")
            print(
                "4> find shared dns => Find more targets with a DNS server shared record search.")
            print(
                "5> dns propagation => Check whether recent DNS changes have propagated.")
            print("6> find records => Find forward DNS (A) records for a domain.")
            print("7> cloud flare => Find sub-active domains bound to the list.")
            print("8> extract links => Find all web page links. ")
            print("9> web robot => Extract important tags on the web page.")
            print("Exit> exit")
            print("Back> back")
            print("\n")

        while True:
            guide()
            raw = raw_input(R + "WH->" + W)
            if raw == '1':
                master.dns_explore.dnslookup().run()
            elif raw == '2':
                master.dns_explore.domain_map().run()
            elif raw == '3':
                master.dns_explore.dns_report().run()
            elif raw == '4':
                master.dns_explore.find_shared_dns().run()
            elif raw == '5':
                master.dns_explore.dns_propagation().run()
            elif raw == '6':
                master.dns_explore.find_records().run()
            elif raw == '7':
                master.dns_explore.cloud_flare().run()
            elif raw == '8':
                master.dns_explore.extract_links().run()
            elif raw == '9':
                master.dns_explore.web_robot().run()
            elif raw == 'exit':
                sys.exit()
            elif raw == 'back':
                break
            else:
                continue

    def whois_ip():
        def guide():
            print("\n1> reverse ip => Show all sites on the server.")
            print("2> whois ip => Find the geographic location of an IP"
                  " Address.")
            print("3> ip history => Show historical IP addresses for"
                  " a domain.")
            print("4> trace ip using mtr => Trace the Internet connection "
                  "path using the mtr traceroute tool.")
            print("5> trace route => Trace the servers between ViewDNS and"
                  " a remote host.")
            print("Exit> exit")
            print("Back> back\n")

        while True:
            guide()
            raw = raw_input(R + "WH->" + W)
            if raw == '1':
                master.whois_ip.reverse_ip().run()
            elif raw == '2':
                master.whois_ip.whois_ip().run()
            elif raw == '3':
                master.whois_ip.ip_history().run()
            elif raw == '4':
                master.whois_ip.trace_ip().run()
            elif raw == '5':
                master.whois_ip.trace_route().run()
            elif raw == 'exit':
                sys.exit()
            elif raw == 'back':
                break
            else:
                continue

    def panel_brute():
        def guide():
            print("\n1> admin finder asp => Finding page of ASP admin pages.")
            print("2> admin finder php => Finding page of PHP admin pages.")
            print("3> admin finder js => Finding page of JS admin pages.")
            print("4> admin finder cgi => Finding page of CGI admin pages.")
            print("5> admin finder brf => Finding page of BRF admin pages.")
            print("6> boot ini => Find the boot ini file.")
            print("7> etc passwd => Find the etc/passwd file.")
            print("8> etc shadow => Find the etc/shadow file.")
            print("9> file brute => Find the file on server.")
            print("10> direct brute => Find the direct on server.")
            print("11> iis brute => Find the iis page.")
            print("12> log access => Find the log access files.")
            print("13> web service => Find the web service page.")
            print("14> robots txt => Find the robots txt page.")
            print("Exit> exit")
            print("Back> back\n")

        while True:
            guide()
            raw = raw_input(R + "WH->" + W)
            if raw == '1':
                master.panel_brute.admin_asp().run()
            elif raw == '2':
                master.panel_brute.admin_php().run()
            elif raw == '3':
                master.panel_brute.admin_js().run()
            elif raw == '4':
                master.panel_brute.admin_cgi().run()
            elif raw == '5':
                master.panel_brute.admin_brf().run()
            elif raw == '6':
                master.panel_brute.boot_ini().run()
            elif raw == '7':
                master.panel_brute.etc_passwd().run()
            elif raw == '8':
                master.panel_brute.etc_shadow().run()
            elif raw == '9':
                master.panel_brute.file().run()
            elif raw == '10':
                master.panel_brute.directory().run()
            elif raw == '11':
                master.panel_brute.iis().run()
            elif raw == '12':
                master.panel_brute.log_access().run()
            elif raw == '13':
                master.panel_brute.webservice().run()
            elif raw == '14':
                master.panel_brute.robots_txt().run()
            elif raw == 'exit':
                sys.exit()
            elif raw == 'back':
                break
            else:
                continue

    def whois_web():
        def guide():
            print("\n1> whois => Lookup information on a Domain or IP address.")
            print("2> reverse whois => Find domain names owned by an "
                  "individual or company.")
            print("3> reverse ns => Find all sites that use a given"
                  " nameserver.")
            print("4> reverse mx => Find all sites that use a given mail"
                  " server.")
            print("Exit> exit")
            print("Back> back\n")

        while True:
            guide()
            raw = raw_input(R + "WH->" + W)
            if raw == '1':
                master.whois_web.whois().run()
            elif raw == '2':
                master.whois_web.reverse_whois().run()
            elif raw == '3':
                master.whois_web.reverse_ns().run()
            elif raw == '4':
                master.whois_web.reverse_mx().run()
            elif raw == 'exit':
                sys.exit()
            elif raw == 'back':
                break
            else:
                continue

    def foot_printing():
        def guide():
            print("\n1> cms footprint => Checking web for anaysis CMS.")
            print("2> os footprint => Checking opration system.")
            print("3> framework footprint => Analysis web aplications & web"
                  " Frameworks.")
            print("4> language footprint => identifies language web.")
            print("5> waf footprint => footprinting fireWall & Security"
                  " Managers.")
            print("6> httpheaders footprint => Http header footprinting.")
            print("Exit> exit")
            print("Back> back\n")

        while True:
            guide()
            raw = raw_input(R + "WH->" + W)
            if raw == '1':
                master.foot_printing.cms.cms().run()
            elif raw == '2':
                master.foot_printing.os.os().run()
            elif raw == '3':
                master.foot_printing.framework.framework().run()
            elif raw == '4':
                master.foot_printing.language.language().run()
            elif raw == '5':
                master.foot_printing.waf.waf().run()
            elif raw == '6':
                master.foot_printing.httpheader.httpheader().run()
            elif raw == 'exit':
                sys.exit()
            elif raw == 'back':
                break
            else:
                continue

    def scan_automatic():
        def guide():
            print("\n1> scan auto => automaticaly web scanner.")
            print("Exit> exit")
            print("Back> back\n")
        while True:
            guide()
            raw = raw_input(R + "WH->" + W)
            if raw == '1':
                master.scan_automatic.scan_automatic().run()
            elif raw == 'exit':
                sys.exit()
            elif raw == 'back':
                break
            else:
                continue

    def search_engine():
        def guide():
            print("\n1> bing mail => search to bing for mail.")
            print("2> google mail => search to google for mail.")
            print("3> yahoo mail => search to yahoo for mail.")
            print("4> all mail => search to bing google yahoo for mail.")
            print("5> bing hosts => search to bing for hosts and subdomain.")
            print("6> google hosts => search to google for subdomain.")
            print("7> yahoo hosts => search to yahoo for subdomain.")
            print("8> all hosts => search to bing google yahoo for hosts"
                  " subdomain.")
            print("Exit> exit")
            print("Back> back\n")

        while True:
            guide()
            raw = raw_input(R + "WH->" + W)
            if raw == '1':
                master.search_engine.bing_mail().run()
            elif raw == '2':
                master.search_engine.google_mail().run()
            elif raw == '3':
                master.search_engine.yahoo_mail().run()
            elif raw == '4':
                master.search_engine.all_mail().run()
            elif raw == '5':
                master.search_engine.bing_host().run()
            elif raw == '6':
                master.search_engine.google_host().run()
            elif raw == '7':
                master.search_engine.yahoo_host().run()
            elif raw == '8':
                master.search_engine.all_host().run()
            elif raw == 'exit':
                sys.exit()
            elif raw == 'back':
                break
            else:
                continue

    banner()

    while True:
        guide()
        raw = raw_input(R + "WH->" + W)
        if raw == '1':
            dns_explore()
        elif raw == '2':
            whois_ip()
        elif raw == '3':
            panel_brute()
        elif raw == '4':
            whois_web()
        elif raw == '5':
            foot_printing()
        elif raw == '6':
            search_engine()
        elif raw == '7':
            scan_automatic()
        elif raw == 'exit':
            break
        elif raw == '':
            continue
        else:
            continue


if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        print("explore interrupted by user..")
    # except BaseException:
        # sys.exit()
