#!/usr/bin/env python
# -*- coding: utf-8 -*-

# third-party modules
import logging
from flask_caching import Cache
from redis import Redis
from flask import request
import urllib

__author__ = ""
__maintainer__ = ""
__email__ = ""
__copyright__ = ""


def get_redis_client(self):
    redis_client = Redis(
        self.app.config['CACHE_REDIS_HOST'],
        self.app.config['CACHE_REDIS_PORT'],
        self.app.config['CACHE_REDIS_DB'],
        self.app.config['CACHE_REDIS_PASSWORD'],)
    return redis_client

def cache_key(self):
    args = request.args
    key = request.path + '?' + urllib.parse.urlencode([
        (k, v) for k in sorted(args) for v in sorted(args.getlist(k))
    ])
    return key

def clear_cache(self, key_prefix=None):
    redis_client = self.get_redis_client()
    if not key_prefix:
        key_prefix = request.path
    keys = [key for key in redis_client.keys('{}*'.format(key_prefix))]
    nkeys = len(keys)
    for key in keys:
        redis_client.delete(key)
    if nkeys > 0:
        logging.info("Cleared %s cache keys", nkeys)
        logging.info(keys)


Cache.get_redis_client = get_redis_client
Cache.cache_key = cache_key
Cache.clear_cache = clear_cache

cache = Cache()