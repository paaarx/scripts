# Return a http conection when you have proxy
# It is useful when you use a GoogleAPI with httplib2

import httplib2
import os


def http_proxy_connection(proxy_host: str, proxy_port: int):
    os.environ['https_proxy'] = f'{proxy_host}:{proxy_port}'
    return httplib2.Http(disable_ssl_certificate_validation=True)
