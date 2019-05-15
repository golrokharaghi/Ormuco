from collections import OrderedDict
import time

class LRUCache:
    """
        class LRUCache implements a Least Recently Used cache with time expiration

        Parameters:
            size : maximum size of the cache
            expiration : expiration time of the cache (in second)

        Methods:
            __init__(size, expiration) : set the size and expiration time
            get_item(key) : retrieve the corresponding value of a given key
            set_item(key, value) : write the given key, value pair in the cache
            check_expiry() : delete the cashed items if the time since the last access
            is higher than the expiration time (called by get_item and set_item)
            delete(key): delete the given key
            display() : display the cached items
    """

    def __init__(self, size, expiration):
        self.size = size
        self.expiration = expiration
        self.last_access_time = {}
        self.cache = OrderedDict()

    # To get an item, pop it and insert it back to update its timestamp. Also update the access time and check for expiry.
    def get_item(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            self.last_access_time [key] = time.time()
            self.check_expiry()
            return value
        else:
            return ('Key does not exist.')

    # To set an item, pop it and insert it back to update its timestamp. Also update the access time and check for expiry.
    # If the cache is full, remove the least recently used item.
    def set_item(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.size:
            self.cache.popitem(last = False)
        self.cache[key] = value
        self.last_access_time [key] = time.time()
        self.check_expiry()

    # Remove the items from the cache if the time since their last access exceeds the expiration time.
    def check_expiry (self):
        for k in self.last_access_time .keys():
            if time.time() - self.last_access_time [k] > self.expiration:
                self.delete(k)


    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
            del self.last_access_time [key]


    def display(self):
        return self.cache



if __name__ == "__main__":
	    import doctest
	    doctest.testmod()
