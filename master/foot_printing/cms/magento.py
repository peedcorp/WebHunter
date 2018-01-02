#!/usr/bin/env python
# WebHunter MiniModule

import re


class Magento:
    @staticmethod
    def run(content):
        _ = False
        try:
            for x in (
                'x-magento-init', 'Magento_*',
                'images/logo.gif" alt="Magento Commerce" /></a></h1>',
                '<a href="http://www.magentocommerce.com/bug-tracking" id="bug_tracking_link"><strong>Report All Bugs</strong></a>',
                '<meta name="keywords" content="Magento, Varien, E-commerce" />',
                'mage/cookies.js" ></script>',
                    '<div id="noscript-notice" class="magento-notice">'):
                _ = re.search(x, content) is not None
                if _:
                    return "Magento"
                    break
        except Exception as e:
            pass
