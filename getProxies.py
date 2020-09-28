
from lxml.html import fromstring
import requests
import traceback


def get_proxies(n=1):
    """
    Return SOCKS4 type proxy server
    :param n: number of proxies requested (default: 1)
    """
    url = 'https://www.socks-proxy.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = []
    for i in parser.xpath('//tbody/tr')[:n]:
        proxy = ":".join([i.xpath('.//td[1]/text()')[0],
                          i.xpath('.//td[2]/text()')[0]])
        proxies.append(proxy)
    return proxies


if __name__ == '__main__':
    n = input('How many proxy you want? (1-300): ')
    
    try:
        n = int(n)
        proxies = get_proxies(n)
        print(proxies)
    except:
        print('Input error')
