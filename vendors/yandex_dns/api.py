__author__ = 'Vitalyi'

import requests

class YandexDnsApi:

    base_url = 'https://pddimp.yandex.ru/nsapi/'

    def get_token(self, domain_name):
        result = requests.get(self.base_url, params={'domain_name':domain_name})
        pass

    def add_a_record(self, domain, content, subdomain=None, ttl=None):
        # token
        pass

    def add_аааa_record(self, domain, content, subdomain=None, ttl=None):
        # token
        pass

    def add_cname_record(self, domain, content, subdomain=None, ttl=None):
        # token
        pass

    def add_mx_record(self, domain, content, subdomain=None, ttl=None,  priority=None):
        # token
        pass

    def add_ns_record(self, domain, content, subdomain=None, ttl=None):
        # token
        pass

    def add_srv_record(self, domain, weight, port, target, subdomain=None, ttl=None, priority=None):
        # token
        pass

    def add_txt_record(selfd, domain, content, subdomain=None, ttl=None):
        # token
        pass

    def get_domain_records(self, domain):
        # token
        pass

    def edit_a_record(self, domain, record_id, content, subdomain=None, ttl=None):
        # token
        pass

    def edit_aaaa_record(self, domain, record_id, content, subdomain=None, ttl=None):
        # token
        pass

    def edit_cname_record(self, domain, record_id, content, subdomain=None, ttl=None):
        # token
        pass

    def edit_mx_record(self, domain, record_id, content, subdomain=None, ttl=None, priority=None):
        # token
        pass

    def edit_ns_record(self, domain, record_id, content, subdomain=None, ttl=None):
        # token
        pass

    def edit_srv_record(self, domain, record_id, weight, port, target, subdomain=None, ttl=None, priority=None):
        # token
        pass

    def edit_soa_record(self, domain, admin_mail, refresh, retry, expire, neg_cache, ttl=None):
        # toke
        pass

    def edit_txt_record(self, domain, record_id, content, subdomain=None, ttl=None):
        # token
        pass

    def delete_record(self, domain, record_id):
        # token
        pass
