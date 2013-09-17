from vendors.yandex_dns.api import YandexDnsApi

__author__ = 'Vitalyi'


class YandexDns:
    api = YandexDnsApi()

    def __init__(self, domain_name):
        self.api.get_token(domain_name)
        pass