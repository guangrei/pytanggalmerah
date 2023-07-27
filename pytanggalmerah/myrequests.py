# -*- coding: utf-8 -*-
import requests
from zcache import Cache
from urllib import parse
import os


class MyRequests(object):
    def __init__(self, url, cache_time, cache_path=None):

        u_en = parse.quote_plus(url)  # url encode
        cache = Cache(path=cache_path)
        if cache.has(u_en):
            self.response = cache.get(u_en)
            self.is_loaded_from_cache = True
        else:
            r = self.makeRequest(url)
            if r != False:
                cache.set(u_en, r, ttl=cache_time)
                cache.set(u_en+"_offline", r)
                self.response = r
                self.is_loaded_from_cache = False
            else:
                self.response = cache.get(u_en+"_offline")
                self.is_loaded_from_cache = True

    def makeRequest(self, url):

        try:
            req = requests.get(url)
            return req.text
        except:
            return False
