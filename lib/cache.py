from google.appengine.api import memcache

class cached:
    def __init__(self, key, expire=60, identifier=None):
        self.key = key
        self.expire = expire
        self.identifier = identifier
        
    def __call__(self, function):
        def cache_wrapper(*args, **kwds):
            key = self.key
            
            if self.identifier is not None:
                try:
                    key = "%s_%s" % (str(self.key), str(kwds[self.identifier]))
                except KeyError:
                    key = self.key

            cached_result = memcache.get(key)
            
            if cached_result is not None:
                return cached_result
            else:
                result = function(*args, **kwds)
                memcache.add(key, result, self.expire)
                return result
        
        return cache_wrapper