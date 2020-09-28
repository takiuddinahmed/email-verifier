from getProxies import get_proxies
from verifier.verifier import Verifier
import random


def verify(addr, **kwargs):
    v = Verifier(source_addr='user@example.com', **kwargs)
    print(v)
    result = v.verify(addr)
    return result


if __name__ == '__main__':
    # addr = input('Enter email to verify: ')
    addr = 'example@example.com'
    proxy_status_input = input('Do you want to use default proxy : (y/n)')
    proxy_status = False
    if proxy_status_input.lower() == 'y':
        proxy_status = True
    if proxy_status:
        proxy = get_proxies(10)[random.randint(0, 9)]
        proxy_addr, proxy_port = proxy.split(':')
        proxy_port = int(proxy_port)
        proxy_type = 'socks4'
        result = verify(addr, proxy_type=proxy_type,
                        proxy_addr=proxy_addr, proxy_port=proxy_port)
        print(result)
    else:
        result = verify(addr)
        print(result)
